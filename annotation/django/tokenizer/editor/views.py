from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Import reverse_lazy method for reversing names to URLs
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import resolve
from . import models
from django.contrib.auth.models import User, Group
from django.db.models import Q

# Import the login_required decorator which can be applied to
# views to enforce that the user should be logged in to access the
# view
from django.contrib.auth.decorators import login_required

import re
import cgi
import editor.html2text
import random
import codecs
import json

re_string = re.compile(r'(?P<htmlchars>[<&>])|(?P<space>^[ \t]+)|(?P<lineend>\r\n|\r|\n)|(?P<protocal>(^|\s)((http|ftp)://.*?))(\s|$)', re.S|re.M|re.I)
def plaintext2html(text, tabstop=4):
    def do_sub(m):
        c = m.groupdict()
        if c['htmlchars']:
            return cgi.escape(c['htmlchars'])
        if c['lineend']:
            return '<br>'
        elif c['space']:
            t = m.group().replace('\t', '&nbsp;'*tabstop)
            t = t.replace(' ', '&nbsp;')
            return t
        elif c['space'] == '\t':
            return ' '*tabstop;
        else:
            url = m.group('protocal')
            if url.startswith(' '):
                prefix = ' '
                url = url[1:]
            else:
                prefix = ''
            last = m.groups()[-1]
            if last in ['\n', '\r', '\r\n']:
                last = '<br>'
            return '%s<a href="%s">%s</a>%s' % (prefix, url, url, last)
    return re.sub(re_string, do_sub, text)

r1 = re.compile(ur'[\n\r\f\v][\n\r\f\v]+', re.U) # multiple empty lines
r2 = re.compile(ur'[ \t\ufeff\u00a0\u2028\u2029\u0020\u3000]+', re.U) # spaces
r3 = re.compile(ur'^[ \t\ufeff\u00a0\u2028\u2029\u0020\u3000]+', re.U|re.M) # leading spaces in each line
r4 = re.compile(ur'[ \t\ufeff\u00a0\u2028\u2029\u0020\u3000]+$', re.U|re.M) # trailing spaces in each line
r5 = re.compile(ur'^[ \t\n\r\f\v\ufeff\u00a0\u2028\u2029\u0020\u3000]+', re.U) # leading spaces overall
r6 = re.compile(ur'[ \t\n\r\f\v\ufeff\u00a0\u2028\u2029\u0020\u3000]+$', re.U) # trailing spaces overall
r7 = re.compile(ur'[\'"]') # quotes
def process_text(text):
    sub1 = re.sub(r1, '\n\n', text)
    sub2 = re.sub(r2, ' ', sub1)
    sub3 = re.sub(r3, '', sub2)
    sub4 = re.sub(r4, '', sub3)
    sub5 = re.sub(r5, '', sub4)
    sub6 = re.sub(r6, '', sub5)
    sub7 = re.sub(r7, '`', sub6)
    return sub7

r_newline = re.compile(r'\n', re.U)
def preprocess_for_diff(text):
    return re.sub(r_newline, ' ', text);

def apply_regex_fiexes(text):
    for fix in models.RegexFix.objects.all():
        text = re.sub(fix.pattern, fix.replacement, text)
    return text

# This view handles the request to the root URL /. For the mapping,
# check urls.py
def index(request):
    # The current user object is available as request.user. If the
    # user is authenticated, is_authenticated() method of the User
    # object returns True, else it returns False. If the user is logged in
    # redirect to the home page, else to the login page.
    # reverse_lazy() method takes a URL pattern name and returns the URL path.
    # Here it is used to get the URL paths of home and login pages.
    if request.user.is_authenticated():
        return redirect(reverse_lazy('workspace_editor'))
    else:
        return redirect(reverse_lazy('login_editor'))
  
# login_required decorator, when applied to a view enforces the rule that
# a user has to be logged in to the access the view. If he is not logged in,
# he is redirected to the login page.
@login_required
def workspace(request):
    status = models.Status.objects.get(id = 2) # under jurisdiction
    status_na = models.Status.objects.get(id = 1) # na
    status_done = models.Status.objects.get(id = 3) # done
    fileset1 = models.TextFile.objects.filter(first_worker = request.user)#.filter(first_worker_state = status)
    fileset2 = models.TextFile.objects.filter(second_worker = request.user)#.filter(second_worker_state = status)
    fileset_adjudicate = models.TextFile.objects.filter(judge = request.user)
    files_to_judge = fileset_adjudicate.filter(jurisdiction_state = status)
    context = {
        'username':request.user.username,
        'fileset1': fileset1,
        'fileset2': fileset2,
        'files_to_judge': files_to_judge,
        'n_annotation_done': len(fileset1.filter(first_worker_state = status_done)) + len(fileset2.filter(second_worker_state = status_done)),
        'n_annotation_total': len(fileset1.exclude(first_worker_state = status_na)) + len(fileset2.exclude(second_worker_state = status_na)),
        'n_adjudication_done': len(fileset_adjudicate.filter(jurisdiction_state = status_done)),
        'n_adjudication_total': len(fileset_adjudicate.exclude(jurisdiction_state = status_na)),
    }
    return render(request, "editor/workspace.html", context)

@login_required
def workspace_root(request): # this is pure hack to work around the url issue!!
    is_editor_admin = request.user.groups.filter(name='editor_admin').exists()
    is_ner_user = request.user.groups.filter(Q(name='ner_annotator') | Q(name='ner_adjudicator')).exists()
    context = {
        'username': request.user.username,
        'is_ner_user': is_ner_user,
        'is_editor_admin': is_editor_admin
    }
    return render(request, "editor/workspace_root.html", context)

@login_required
def admin_overview(request):
    is_editor_admin = request.user.groups.filter(name='editor_admin').exists()

    status_na = models.Status.objects.get(id = 1) # na
    status_done = models.Status.objects.get(id = 3) # done
    total_assigned = len(models.TextFile.objects.filter(~Q(first_worker_state = status_na)))
    total_tokenized = len(models.TextFile.objects.filter(first_worker_state = status_done))
    total_adjudicated = len(models.TextFile.objects.filter(jurisdiction_state = status_done))
    users = models.User.objects.all()
    print users
    user_progresses = []
    for user in users:
        user_progresses.append({
            'username': user.username,
            'num_assigned': len(models.TextFile.objects.filter(first_worker = user).filter(~Q(first_worker_state = status_na))),
            'num_completed': len(models.TextFile.objects.filter(first_worker = user).filter(first_worker_state = status_done)),
            'num_jurisdiction_assigned': len(models.TextFile.objects.filter(judge = user).filter(~Q(jurisdiction_state = status_na))),
            'num_jurisdiction_completed': len(models.TextFile.objects.filter(judge = user).filter(jurisdiction_state = status_done))
        })

    print user_progresses

    context = {
        'username': request.user.username,
        'total_assigned': total_assigned,
        'total_tokenized': total_tokenized,
        'total_adjudicated': total_adjudicated,
        'user_progresses': user_progresses
    }
    if (is_editor_admin):
        return render(request, "editor/admin_overview.html", context)
    else:
        response = HttpResponse("Not authorized!")
        response.status_code = 403
        return response

@login_required
def instruction(request):
    context = {'user': request.user}
    return render(request, "editor/instruction.html", context)

@login_required
def tokenize_text(request, file_id, file_copy):
    file_to_edit = models.TextFile.objects.get(pk=file_id)
    # validate request
    if (file_copy == "1"):
        if (request.user != file_to_edit.first_worker):
            response = HttpResponse("Not authorized!")
            response.status_code = 403
            return response
    if (file_copy == "2"):
        if (request.user != file_to_edit.second_worker):
            response = HttpResponse("Not authorized!")
            response.status_code = 403
            return response    

    if (file_copy == "1"):
        comment_block = file_to_edit.first_worker_comment.encode('UTF-8')
        file_state = file_to_edit.first_worker_state.id
        text_content = plaintext2html(process_text(file_to_edit.file_content1))
    elif (file_copy == "2"):
        comment_block = file_to_edit.second_worker_comment.encode('UTF-8')
        file_state = file_to_edit.second_worker_state.id
        text_content = plaintext2html(process_text(file_to_edit.file_content2))

    status = models.Status.objects.get(id = 3) # "DONE" status
    my_files = models.TextFile.objects.filter((Q(first_worker = request.user) & ~Q(first_worker_state = status)) | (Q(second_worker = request.user) & ~Q(second_worker_state = status)))
    prev_files = my_files.filter(id__lt = file_id)
    next_files = my_files.filter(id__gt = file_id)
    if prev_files.exists():
        prev_file = prev_files[len(prev_files) - 1]
        prev_file_url = reverse_lazy('tokenize_text', args=(prev_file.id,))
    else:
        prev_file_url = reverse_lazy('workspace_editor')
    if next_files.exists():
        next_file_url = reverse_lazy('tokenize_text', args=(next_files[0].id,))
    else:
        next_file_url = reverse_lazy('workspace_editor')

    context = {'username': request.user.username,
               'title': file_to_edit.file_name,
               'file_copy':file_copy,
               'text_content': text_content,
               'comment_content': comment_block,
               'file_state': file_state,
               'prev_file_url': prev_file_url,
               'next_file_url': next_file_url}
    return render(request, "editor/tokenize_text.html", context)

@login_required
def jurisdiction(request, file_id):
    file_to_compare = models.TextFile.objects.get(pk=file_id)
    # validate the request
    if (request.user != file_to_compare.judge):
        response = HttpResponse("Not authorized!")
        response.status_code = 403
        return response

    annotator1 = file_to_compare.first_worker.username
    annotator2 = file_to_compare.second_worker.username
    comment1 = file_to_compare.first_worker_comment
    comment2 = file_to_compare.second_worker_comment
    text_content1 = file_to_compare.file_content1
    text_content2 = file_to_compare.file_content2
    processed_text_content1 = preprocess_for_diff(apply_regex_fiexes(process_text(text_content1))).encode('UTF-8')
    processed_text_content2 = preprocess_for_diff(apply_regex_fiexes(process_text(text_content2))).encode('UTF-8')

    # initial final text
    if (len(file_to_compare.file_content_final)==0):
        initial_final_text = plaintext2html(process_text(text_content1))
    else:
        initial_final_text = plaintext2html(process_text(file_to_compare.file_content_final))

    status = models.Status.objects.get(id = 2) # under jurisdiction
    my_files = models.TextFile.objects.filter(judge = request.user).filter(jurisdiction_state = status)
    prev_files = my_files.filter(id__lt = file_id)
    next_files = my_files.filter(id__gt = file_id)
    if prev_files.exists():
        prev_file = prev_files[len(prev_files) - 1]
        prev_file_url = reverse_lazy('jurisdiction', args=(prev_file.id,))
    else:
        prev_file_url = reverse_lazy('workspace_editor')
    if next_files.exists():
        next_file_url = reverse_lazy('jurisdiction', args=(next_files[0].id,))
    else:
        next_file_url = reverse_lazy('workspace_editor')

    # assemble context
    context = {'username': request.user.username,
               'title': file_to_compare.file_name,
               'file_copy':"3",
               'text_content1': json.dumps(str(processed_text_content1))[1:-1],   # hack to remove the quotes
               'text_content2': json.dumps(str(processed_text_content2))[1:-1],
               'initial_final_text': initial_final_text,
               'comment1': editor.html2text.html2text(comment1),
               'comment2': editor.html2text.html2text(comment2),
               'annotator1': annotator1,
               'annotator2': annotator2,
               'prev_file_url': prev_file_url,
               'next_file_url': next_file_url}
    return render(request, "editor/jurisdiction.html", context)


def save_tokenized(request): 
    if request.method == "POST":
        htmlText = request.POST.get("text_content")
        fileName = request.POST.get("file_name")
        fileCopy = request.POST.get("file_copy")
        comment = request.POST.get("comment_content")
        fp = models.TextFile.objects.get(file_name = fileName)

        # validate the request
        if (fileCopy == "1"):
            if (request.user != fp.first_worker):
                response = HttpResponse("Not authorized!")
                response.status_code = 403
                return response
        elif (fileCopy == "2"):
            if (request.user != fp.second_worker):
                response = HttpResponse("Not authorized!")
                response.status_code = 403
                return response   
        elif (fileCopy == "3"):
            if (request.user != fp.judge):
                response = HttpResponse("Not authorized!")
                response.status_code = 403
                return response   

        # save text
        plainText = process_text(editor.html2text.html2text(htmlText))
        if fileCopy == "1":
            fp.file_content1 = plainText
        if fileCopy == "2":
            fp.file_content2 = plainText
        if fileCopy == "3":
            fp.file_content_final = plainText

        # update status labels
        statusSubmitted = models.Status.objects.get(id=3) # submitted file
        statusDirty = models.Status.objects.get(id=4) # dirtied file
        
        if (fileCopy == "1"):
            if (fp.first_worker_state != statusSubmitted):
                fp.first_worker_comment = comment.encode('UTF-8')
                fp.first_worker_state = statusDirty
        elif (fileCopy == "2"):
            if (fp.second_worker_state != statusSubmitted):
                fp.second_worker_comment = comment.encode('UTF-8')
                fp.second_worker_state = statusDirty
        fp.save()

        response = HttpResponse("Success")
        response.status_code = 204
        return response
    else:
        response = HttpResponse()
        response.status_code = 501
        return response

def submit_tokenized(request): 
    if request.method == "POST":
        fileName = request.POST.get("file_name")
        fileCopy = request.POST.get("file_copy")
        f = models.TextFile.objects.get(file_name = fileName)

        # validate request
        if (fileCopy == "1"):
            if (request.user != f.first_worker):
                response = HttpResponse("Not authorized!")
                response.status_code = 403
                return response
        elif (fileCopy == "2"):
            if (request.user != f.second_worker):
                response = HttpResponse("Not authorized!")
                response.status_code = 403
                return response   
        elif (fileCopy == "3"):
            if (request.user != f.judge):
                response = HttpResponse("Not authorized!")
                response.status_code = 403
                return response   

        # submit it to database
        status = models.Status.objects.get(id = 3) # "DONE" status
        if (fileCopy == "1"):
            f.first_worker_state = status
        elif (fileCopy == "2"):
            f.second_worker_state = status
        else:
            f.jurisdiction_state = status

        # is there concurrency issue here?
        if ((f.jurisdiction_state != status) and (f.first_worker_state == status) and (f.second_worker_state == status)):
            status = models.Status.objects.get(id = 2) # "IN" in progress status
            judgeToBe = ""
            while True:
                judgeToBe = Group.objects.get(name='adjudicator').user_set.order_by('?').first()              
                if (judgeToBe.id != f.first_worker.id and judgeToBe.id != f.second_worker.id):
                    break

            ### ad-hoc rules ###

            if ((f.first_worker.id == 15) or (f.first_worker.id == 16) or (f.first_worker.id == 19)):
                judgeToBe = User.objects.get(pk = 18)

            if ((f.first_worker.id == 18) or (f.first_worker.id == 17)):
                judgeToBe = User.objects.get(pk = 8)            

            ####################


            f.judge = judgeToBe
            f.jurisdiction_state = status

        f.save()

        response = HttpResponse("Success")
        response.status_code = 204
        return response
    else:
        response = HttpResponse()
        response.status_code = 501
        return response
