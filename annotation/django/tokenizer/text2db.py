# -*- coding: utf-8 -*-
import random
import re
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tokenizer.settings")

import django
django.setup()

from django.contrib.auth.models import User, Group
from editor import models

import codecs
import math

#textFiles = models.TextFile.objects.filter(id__gt=58) # the new file set
#statusIn = models.Status.objects.get(pk=2) # task assigned but not started
fixes = models.RegexFix.objects.all()

# workers = []*5
# workers.append(User.objects.get(pk=15)) #lurenjia
# workers.append(User.objects.get(pk=16)) #2013172079
# workers.append(User.objects.get(pk=17)) #beibei123dan
# workers.append(User.objects.get(pk=18)) #liubieren
# workers.append(User.objects.get(pk=1)) #default user


#i = 0

#for fEntry in textFiles:
#    print(fEntry.file_name)
#    if (fEntry.first_worker_state == statusIn):
#        filePath = "editor/data/original/rand/" + fEntry.file_name # assemble the file path on my local computer, where the pre-tokenized files are located
#        f = codecs.open(filePath, 'r', 'utf-8')
#        textContent = f.read()
#        fEntry.file_content_original = textContent
#        fixed_content = textContent
#        for fix in fixes:
#            fixed_content = re.sub(fix.pattern, fix.replacement, fixed_content)
#        fEntry.file_content1 = fixed_content
#        fEntry.file_content2 = fixed_content
#        f.close()
#        fEntry.save()
#        print("done")
#    else:
#        print("skipped")

WORKER_ID = 20
status_na = models.Status.objects.get(pk=1)
status_in = models.Status.objects.get(pk=2)
status_done = models.Status.objects.get(pk=3)

N_FILES_TO_ADD = 100

with open('/Users/Chen/Downloads/rand2/ranList2.txt') as f:
    lines = f.readlines()
file_list = [line[:-2] for line in lines]

for file_name in file_list[3*N_FILES_TO_ADD:4*N_FILES_TO_ADD]:
    print 'assigning %s' % file_name
    text_file = models.TextFile()
    filePath = '/Users/Chen/Downloads/rand2/%s' % file_name
    f = codecs.open(filePath, 'r', 'utf-8')
    textContent = f.read()
    fixed_content = textContent
    for fix in fixes:
        fixed_content = re.sub(fix.pattern, fix.replacement, fixed_content)
    f.close()

    text_file.file_name = file_name
    text_file.file_location = ''
    text_file.first_worker = User.objects.get(pk=WORKER_ID)
    text_file.first_worker_state = status_in
    text_file.first_worker_comment = u'请在此处留下评论。有任何不确定的疑问也请在此处留下。'
    text_file.second_worker = User.objects.get(pk=1)
    text_file.second_worker_state = status_done
    text_file.second_worker_comment = u'请在此处留下评论。有任何不确定的疑问也请在此处留下。'
    text_file.judge = User.objects.get(pk=1)
    text_file.jurisdiction_state = status_na
    text_file.file_content1 = fixed_content
    text_file.file_content2 = fixed_content
    text_file.file_content_final = ''
    text_file.file_content_original = textContent

    text_file.save()
