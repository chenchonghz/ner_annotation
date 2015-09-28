from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from . import models
from . import tasks
from . import term_matching
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Count

import logging

logger = logging.getLogger(__name__)

class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def index(request):
    if request.user.is_authenticated():
        return redirect(reverse_lazy('workspace_ner'))
    else:
        return redirect(reverse_lazy('login_ner'))

@login_required
def workspace(request):
    is_adjudicator = request.user.groups.filter(name='ner_adjudicator').exists()
    fileset_annotate = models.TextFile.objects.filter(annotator = request.user)
    fileset_adjudicate = models.TextFile.objects.filter(adjudicator = request.user)
    context = {
        'username': request.user.username, 
        'fileset_annotate': fileset_annotate,
        'fileset_adjudicate': fileset_adjudicate,
        'is_adjudicator': is_adjudicator,
        'n_annotation_done': len(fileset_annotate.filter(annotation_state = 'DONE')),
        'n_annotation_total': len(fileset_annotate.exclude(annotation_state = 'NOT_ASSIGNED')),
        'n_adjudication_done': len(fileset_adjudicate.filter(jurisdiction_state = 'DONE')),
        'n_adjudication_total': len(fileset_adjudicate.exclude(jurisdiction_state = 'NOT_READY')),
    }
    return render(request, "ner/workspace.html", context)

@login_required
def annotate_text(request, file_id):
    file_obj = models.TextFile.objects.get(pk = file_id)
    # validate request
    if (request.user != file_obj.annotator):
        response = HttpResponse("Not authorized!")
        response.status_code = 403
        return response
    file_name = file_obj.file_name
    file_content = file_obj.file_content
    file_state = file_obj.annotation_state
    annotation_comment = file_obj.annotation_comment
    categories = models.Category.objects.all()
    result_set = models.AnnotationResult.objects.filter(text_file = file_id)
    my_files = models.TextFile.objects.filter(annotator = request.user)
    prev_files = my_files.filter(id__lt = file_id)
    next_files = my_files.filter(id__gt = file_id)
    if prev_files.exists():
        prev_file = prev_files[len(prev_files) - 1]
        if prev_file.umls_state == 'NOT_READY':
            prev_file_url = reverse_lazy('annotate_text', args=(prev_file.id,))
        else:
            prev_file_url = reverse_lazy('map_umls_terms', args=(prev_file.id,))
    else:
        prev_file_url = reverse_lazy('workspace_ner')
    if next_files.exists():
        if next_files[0].umls_state == 'NOT_READY':
            next_file_url = reverse_lazy('annotate_text', args=(next_files[0].id,))
        else:
            next_file_url = reverse_lazy('map_umls_terms', args=(next_files[0].id,))
    else:
        next_file_url = reverse_lazy('workspace_ner')
    context = {'username': request.user.username,
               'file_name': file_name, 
               'file_content': file_content,
               'file_state': file_state,
               'annotation_comment': annotation_comment,
               'categories': categories,
               'result_set': result_set,
               'umls_url': reverse_lazy('map_umls_terms', args=(file_id,)),
               'prev_file_url': prev_file_url,
               'next_file_url': next_file_url}
    return render(request, 'ner/annotate_text.html', context)

@login_required
def annotation_jurisdiction(request, file_id):
    file_obj = models.TextFile.objects.get(pk = file_id)
    # validate request
    if (request.user != file_obj.adjudicator):
        response = HttpResponse("Not authorized!")
        response.status_code = 403
        return response
    file_obj = models.TextFile.objects.get(pk = file_id)
    file_name = file_obj.file_name
    file_content = file_obj.file_content
    file_state = file_obj.annotation_state
    annotation_comment = file_obj.annotation_comment
    categories = models.Category.objects.all()
    result_set = models.AnnotationResult.objects.filter(text_file = file_id)
    my_files = models.TextFile.objects.filter(adjudicator = request.user).filter(jurisdiction_state = 'IN_PROGRESS')
    prev_files = my_files.filter(id__lt = file_id)
    next_files = my_files.filter(id__gt = file_id)
    if prev_files.exists():
        prev_file = prev_files[len(prev_files) - 1]
        prev_file_url = reverse_lazy('annotation_jurisdiction', args=(prev_file.id,))
    else:
        prev_file_url = reverse_lazy('workspace_ner')
    if next_files.exists():
        next_file_url = reverse_lazy('annotation_jurisdiction', args=(next_files[0].id,))
    else:
        next_file_url = reverse_lazy('workspace_ner')
    context = {'username': request.user.username,
               'file_name': file_name, 
               'file_content': file_content,
               'file_state': file_state,
               'annotation_comment': annotation_comment,
               'categories': categories,
               'result_set': result_set,
               'umls_url': reverse_lazy('map_umls_terms', args=(file_id,)),
               'prev_file_url': prev_file_url,
               'next_file_url': next_file_url}
    return render(request, 'ner/annotation_jurisdiction.html', context)

@login_required
def map_umls_terms(request, file_id):
    file_obj = models.TextFile.objects.get(pk = file_id)
    # validate request
    if (request.user != file_obj.annotator):
        response = HttpResponse("Not authorized!")
        response.status_code = 403
        return response
    file_name = file_obj.file_name
    file_content = file_obj.file_content
    file_state = file_obj.umls_state
    umls_comment = file_obj.umls_comment
    categories = models.Category.objects.all()
    result_set = models.AnnotationResult.objects.filter(text_file = file_id)
    preloaded_umls_lookup_results = []
    for result in result_set:
        lookup = models.UmlsLookupResult.objects.filter(source = result.token_text)
        if lookup.exists():
            preloaded_umls_lookup_results.append(lookup.get())
    my_files = models.TextFile.objects.filter(annotator = request.user)
    prev_files = my_files.filter(id__lt = file_id)
    next_files = my_files.filter(id__gt = file_id)
    if prev_files.exists():
        prev_file = prev_files[len(prev_files) - 1]
        if prev_file.umls_state == 'NOT_READY':
            prev_file_url = reverse_lazy('annotate_text', args=(prev_file.id,))
        else:
            prev_file_url = reverse_lazy('map_umls_terms', args=(prev_file.id,))
    else:
        prev_file_url = reverse_lazy('workspace_ner')
    if next_files.exists():
        if next_files[0].umls_state == 'NOT_READY':
            next_file_url = reverse_lazy('annotate_text', args=(next_files[0].id,))
        else:
            next_file_url = reverse_lazy('map_umls_terms', args=(next_files[0].id,))
    else:
        next_file_url = reverse_lazy('workspace_ner')
    context = {'username': request.user.username,
               'file_name': file_name, 
               'file_content': file_content,
               'file_state': file_state,
               'umls_comment': umls_comment,
               'categories': categories,
               'result_set': result_set,
               'annotation_url': reverse_lazy('annotate_text', args=(file_id,)),
               'preloaded_umls_lookup_results': preloaded_umls_lookup_results,
               'prev_file_url': prev_file_url,
               'next_file_url': next_file_url}
    return render(request, 'ner/map_umls_terms.html', context)

@login_required
def umls_jurisdiction(request):
    # obtain all the tokens (words) that have been mapped
    ars = models.AnnotationResult.objects.exclude(umls_id = '').exclude(umls_id = '""').filter(jurisdiction_state='PENDING').values("token_text", "umls_id").annotate(Count("umls_id")).order_by("-token_text")
    tokens = []
    for ar in ars:
        # extract essential information from umls_id
        ar['umls_id'] = [item.encode('UTF-8') for item in (json.loads(ar['umls_id']))['AUI']]
        # transform dictionary to object
        tokens.append(Struct(**ar))
    context = {'username': request.user.username,
               'tokens': tokens}
    return render(request, 'ner/umls_jurisdiction.html', context)

def decide_umls_jurisdiction(request):
    if request.method == "POST":
        request_data = request.POST
        decision_type = request_data.get("decision_type")
        token_text = request_data.get("token_text")
        umls_id = request_data.get("umls_id").replace('"',"").replace(", ",",").replace("'",'"')

        ars = models.AnnotationResult.objects.filter(token_text = token_text).filter(umls_id__icontains = umls_id)
        if (decision_type == 'accept'):
            for ar in ars:
                (cui, lui, en, aui) = json.loads(ar.umls_id)['AUI']
                if ar.jurisdiction_state != 'ACCEPTED':
                    ar.jurisdiction_state = 'ACCEPTED'
                    accepted = True
                elif ar.jurisdiction_state == 'ACCEPTED':
                    ar.jurisdiction_state = 'PENDING'
                    accepted = False
                ar.save()
            if accepted:
                term_matching.insert_umls_mapping(ar.token_text, en, cui, lui)
            else:
                term_matching.delete_umls_mapping(ar.token_text, en, cui, lui)
        elif (decision_type == 'deny'):
            for ar in ars:
                if ar.jurisdiction_state != 'DENIED':
                    ar.jurisdiction_state = 'DENIED'
                elif ar.jurisdiction_state == 'DENIED':
                    ar.jurisdiction_state = 'PENDING'
                ar.save()
        response = HttpResponse("Success")
        response.status_code = 204
        return response
    else:
        response = HttpResponse()
        response.status_code = 501
        return response

def umls_jurisdiction_edit(request):
    if request.method == "POST":
        response = HttpResponse("Success")
        response.status_code = 204

        request_data = request.POST
        token_text = request_data.get("token_text")
        new_umls_id = request_data.get("new_umls_id")
        previous_umls_id = request_data.get("previous_umls_id")

        ars_to_edit = models.AnnotationResult.objects.filter(token_text=token_text).filter(umls_id__icontains = previous_umls_id)
        for ar in ars_to_edit:
            ar.umls_id = new_umls_id
            ar.save()
        
        return response
    else:
        response = HttpResponse()
        response.status_code = 501
        return response

def save_annotation(request): 
    if request.method == "POST":
        request_data = request.POST
        file_name = request_data.get("file_name")
        results = json.loads(request_data.get("results"))
        comment_text = request_data.get("comment_text")

        text_file = models.TextFile.objects.get(file_name=file_name)

        # validate request
        if (request.user != text_file.annotator):
            response = HttpResponse("Not authorized!")
            response.status_code = 403
            return response

        annotations = models.AnnotationResult.objects.filter(text_file = text_file)

        categories = models.Category.objects.all()
        category_lookup = {}
        for category in categories:
            category_lookup[category.name] = category.id

        existing_annotation_ids = [result.id for result in annotations]
        current_annotation_ids = []

        for i in range(len(results)):
            if not annotations.filter(start_position = results[i].get('start_position'), end_position = results[i].get('end_position')).exists():
                ar = models.AnnotationResult()
                ar.text_file = text_file
                ar.start_position = results[i].get('start_position')
                ar.end_position = results[i].get('end_position')
                ar.token_text = results[i].get('text')
                ar.concept_id = 0 # placeholder
                ar.jurisdiction_state = 'NOT_READY'
                ar.category_id = category_lookup[results[i].get('category_name')]
                # verified_umls_mapping = term_matching.umls_lookup_verified_match_only(results[i].get('text'))
#                 if verified_umls_mapping:
#                     ar.umls_id = json.dumps({
#                         "AUI": [verified_umls_mapping[0], verified_umls_mapping[1], verified_umls_mapping[2], "auto"],
#                         "AUIManualMode":True
#                     })
                ar.save()
            else:
                ar = annotations.get(start_position = results[i].get('start_position'), end_position = results[i].get('end_position'))
                if ar.category_id != category_lookup[results[i].get('category_name')]:
                    ar.category_id = category_lookup[results[i].get('category_name')]
                    ar.save()
                current_annotation_ids.append(ar.id)
#             tasks.preload_umls_lookup.delay(ar.token_text)

        removed_annotation_ids = [id for id in existing_annotation_ids if id not in current_annotation_ids]
        for id in removed_annotation_ids:
            models.AnnotationResult.objects.get(id = id).delete()

        text_file.annotation_comment = comment_text
        text_file.annotation_state = "DIRTY"
        text_file.save()

        response = HttpResponse("Success")
        response.status_code = 204
        return response
    else:
        response = HttpResponse()
        response.status_code = 501
        return response

def submit_annotation(request): 
    if request.method == "POST":
        request_data = request.POST
        file_id = request_data.get("file_id")
        file_name = request_data.get("file_name")
        text_file = models.TextFile.objects.get(file_name = file_name)
        submit_type = request_data.get("submit_type")

        # validate request
        if (request.user != text_file.annotator):
            response = HttpResponse("Not authorized!")
            response.status_code = 403
            return response

        if (submit_type == "annotation"):
#             print "shit"
            text_file.annotation_state = "DONE"
            # text_file.jurisdiction_state = "IN_PROGRESS"
            # text_file.umls_state = "IN_PROGRESS"
        elif (submit_type == "jurisdiction"):
            text_file.jurisdiction_state = "DONE"
            tokens_to_update = models.AnnotationResult.objects.filter(text_file=text_file)
            for token in tokens_to_update:
                token.jurisdiction_state = "PENDING"
                token.save()

        text_file.save()

        response = HttpResponse("Success")
        response.status_code = 204
        return response
    else:
        response = HttpResponse()
        response.status_code = 501
        return response

def umls_lookup(request):
    if request.method == "POST":
        source = request.POST.get("token_text")
        ur = models.UmlsLookupResult.objects.filter(source = source)
        if len(ur) == 1 and len(ur[0].result) > 0:
            result = ur[0].result
        else:
            result = json.dumps(term_matching.umls_lookup(source))
            ur = models.UmlsLookupResult()
            ur.source = source
            ur.algorithm_version = term_matching.UMLS_LOOKUP_ALGORITHM_VERSION
            ur.result = result
            ur.save()
        return HttpResponse(result, content_type="application/json")
    else:
        response = HttpResponse()
        response.status_code = 501
        return response

def umls_lookup_with_translation(request):
    if request.method == "POST":
        translation = request.POST.get("target_text")
        result = json.dumps(term_matching.umls_lookup_with_translation(translation))
        return HttpResponse(result, content_type="application/json")
    else:
        response = HttpResponse()
        response.status_code = 501
        return response

def save_umls_mapping(request):
    if request.method == "POST":
        request_data = request.POST
        file_name = request_data.get("file_name")
        results = json.loads(request_data.get("results"))
        comment_text = request_data.get("comment_text")

        text_file = models.TextFile.objects.get(file_name=file_name)

        # validate request
        if (request.user != text_file.annotator):
            response = HttpResponse("Not authorized!")
            response.status_code = 403
            return response

        annotations = models.AnnotationResult.objects.filter(text_file = text_file)
        for result in results:
            ar = annotations.get(start_position = result['start_position'], end_position = result['end_position'])
            if ar.umls_id != result['umls_id'] or ar.jurisdiction_state != 'PENDING':
                ar.umls_id = result['umls_id']
                ar.jurisdiction_state = 'PENDING'
                ar.save()

        text_file.umls_comment = comment_text
        text_file.umls_state = "DIRTY"
        text_file.save()

        response = HttpResponse("Success")
        response.status_code = 204
        return response
    else:
        response = HttpResponse()
        response.status_code = 501
        return response

def submit_umls_mapping(request):
    if request.method == "POST":
        request_data = request.POST
        file_id = request_data.get("file_id")
        file_name = request_data.get("file_name")
        text_file = models.TextFile.objects.get(file_name = file_name)

        # validate request
        if (request.user != text_file.annotator):
            response = HttpResponse("Not authorized!")
            response.status_code = 403
            return response

        text_file.annotation_state = "DONE"
        text_file.umls_state = "DONE"

        text_file.save()

        response = HttpResponse("Success")
        response.status_code = 204
        return response
    else:
        response = HttpResponse()
        response.status_code = 501
        return response
