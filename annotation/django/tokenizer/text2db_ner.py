# -*- coding: utf-8 -*-
import random
import re
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tokenizer.settings")
import os

import django
django.setup()

from django.contrib.auth.models import User, Group
from ner import models

import codecs

WORKER_ID = 20
worker = User.objects.get(pk=WORKER_ID)
adjudicator = User.objects.get(pk=1) # default user
N_FILES_TO_ADD = 100

for file in os.listdir("test_files/"):
    if not file.endswith(".txt"):
        continue
    file_name = file
    print(file_name + " done!")
    file_path = 'test_files/' + file_name
    f = codecs.open(file_path, 'r', 'utf-8')
    text_content = f.read()
    f.close()

    text_file = models.TextFile()
    text_file.file_name = file_name
    text_file.file_location = ''
    text_file.annotator = worker
    text_file.annotation_state = 'IN_PROGRESS'
    text_file.annotation_comment = u'Please leave comments here'
    text_file.adjudicator = adjudicator
    text_file.jurisdiction_state = 'NOT_ASSIGNED'
    text_file.umls_state = 'NOT_READY'
    text_file.umls_comment = ''
    text_file.file_content = text_content

    text_file.save()
