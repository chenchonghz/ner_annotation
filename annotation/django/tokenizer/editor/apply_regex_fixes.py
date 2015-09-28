from editor.models import RegexFix, TextFile

import re

text_files = TextFile.objects.all()
fixes = RegexFix.objects.all()

for text_file in text_files:
    print 'applying regex fix to file #%d' % text_file.id
    fixed_content = text_file.file_content_original
    for fix in fixes:
        fixed_content = re.sub(fix.pattern, fix.replacement, fixed_content)
    if text_file.first_worker_state.id == 2:
        text_file.file_content1 = fixed_content
    if text_file.second_worker_state.id == 2:
        text_file.file_content2 = fixed_content
    text_file.save()

print 'DONE'
