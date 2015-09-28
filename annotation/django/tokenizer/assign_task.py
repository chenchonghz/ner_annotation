import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tokenizer.settings")

import django
django.setup()

from django.contrib.auth.models import User, Group
from editor import models

import codecs
import math

fileDir = "editor/data/original/rand/"
f = open(fileDir + "ranList.txt", "r")
fileList = f.read().split("\n")
f.close()

workers = []*5
workers.append(User.objects.get(pk=15)) #路人甲
workers.append(User.objects.get(pk=16)) #2013172079
workers.append(User.objects.get(pk=17)) #beibei123dan
workers.append(User.objects.get(pk=18)) #liubieren
workers.append(User.objects.get(pk=1)) #default user

statusNA = models.Status.objects.get(pk=1)
statusIN = models.Status.objects.get(pk=2)
statusDONE = models.Status.objects.get(pk=3)

for i in range(0,500):
    fileName = fileList[i]
    print(fileName)
    filePath = fileDir + fileName
    f = codecs.open(filePath, 'r', 'utf-8')
    fp = models.TextFile()
    fp.file_name = fileName
    fp.first_worker = workers[math.floor(i/100)]
    fp.first_worker_state = statusIN
    fp.second_worker = workers[4]
    fp.second_worker_state = statusDONE
    fp.judge = workers[4]
    fp.jurisdiction_state = statusNA
    fp.file_content1 = f.read()
    fp.first_worker_comment = "请在此处留下评论。有任何不确定的疑问也请在此处留下。".encode('UTF-8')
    fp.second_worker_comment = "请在此处留下评论。有任何不确定的疑问也请在此处留下。".encode('UTF-8')
    f.close()
    fp.save()