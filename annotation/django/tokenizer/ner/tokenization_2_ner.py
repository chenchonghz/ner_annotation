import editor
import ner

status_done = editor.models.Status.objects.get(pk=3)

editor_text_files = editor.models.TextFile.objects.filter(id__gt=58)
ner_text_files = ner.models.TextFile.objects.all()

WORKER_ID = 8 # shaodian
N_FILES_TO_ASSIGN = 10

count = 0
assigned_file_names = [f.file_name for f in ner_text_files]

for editor_text_file in editor_text_files:
    if editor_text_file.file_name not in assigned_file_names and editor_text_file.jurisdiction_state == status_done:
        count += 1
        new_file = ner.models.TextFile()
        new_file.file_name = editor_text_file.file_name
        new_file.file_location = editor_text_file.file_location
        new_file.annotator = User.objects.get(pk=WORKER_ID)
        new_file.annotation_state = 'IN_PROGRESS'
        new_file.annotation_comment = ''
        new_file.adjudicator = User.objects.get(pk=1)
        new_file.jurisdiction_state = 'NOT_ASSIGNED'
        new_file.umls_state = 'NOT_READY'
        new_file.umls_comment = ''
        new_file.file_content = editor_text_file.file_content_final
        new_file.save()
        if count == N_FILES_TO_ASSIGN:
            break

print 'DONE'
