import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tokenizer.settings")

import django
django.setup()

from django.contrib.auth.models import User, Group
from editor import models

import random

# create groups
annotatorGroup = Group.objects.get(name='annotator')
adjudicatorGroup = Group.objects.get(name='adjudicator')

# # create users
annotators = {'zhou':'zhou', 'shaodian':'shaodian', 'yue':'yue', 'handong':'handong', 'nanfang':'nanfang', 
                 'junyan':'junyan', 'nina':'nina', 'jinsen':'jinsen', 'ying':'ying'}
adjudicators = {'nanfang':'nanfang', 'shaodian':'shaodian'}

# for username in annotators:
#     user = User.objects.create_user(username, '', annotators[username])
#     user.save()
#     annotatorGroup.user_set.add(user)
# annotatorGroup.save()

# for username in adjudicators:
#     user = User.objects.get(username=username)
#     adjudicatorGroup.user_set.add(user)
# adjudicatorGroup.save()

# assign tasks
statusNA = models.Status.objects.get(pk=1)
statusIN = models.Status.objects.get(pk=2)
defaultUser = User.objects.get(pk=1)

numAssigned = {}
userSet = annotatorGroup.user_set

tempSet = set()
for user in userSet.all():
    tempSet.add(user)

for i in range(6,51):
    filename = "A 00 ("+str(i)+").txt"
    firstWorker = ""
    secondWorker = ""
    print(i)
    if len(tempSet) <= 2:
        print(tempSet)
        break
    while True:
        samples = random.sample(tempSet,2)
        firstWorker = samples[0]
        secondWorker = samples[1]
        print(firstWorker.id, secondWorker.id)
        if (adjudicatorGroup.user_set.count() == 2):
            if (firstWorker.groups.filter(name='adjudicator').exists() and secondWorker.groups.filter(name='adjudicator').exists()):
                continue
        if (firstWorker.id != secondWorker.id):
            break
    #f = models.TextFile()
    #f.file_name = filename
    f = models.TextFile.objects.get(file_name=filename)
    f.first_worker = firstWorker
    f.second_worker = secondWorker
    
    if firstWorker.id in numAssigned:
        numAssigned[firstWorker.id] += 1
    else:
        numAssigned[firstWorker.id] = 1
    
    if secondWorker.id in numAssigned:
        numAssigned[secondWorker.id] += 1
    else:
        numAssigned[secondWorker.id] = 1

    if (firstWorker.id in numAssigned) and (numAssigned[firstWorker.id] == 10):
        tempSet.remove(firstWorker)
    if (secondWorker.id in numAssigned) and (numAssigned[secondWorker.id] == 10):
        tempSet.remove(secondWorker)

    

    f.first_worker_comment = "请在此处留下评论。有任何不确定的疑问也请在此处留下。".encode('UTF-8')
    f.second_worker_comment = "请在此处留下评论。有任何不确定的疑问也请在此处留下。".encode('UTF-8')
    f.first_worker_state = statusIN
    f.second_worker_state = statusIN
    f.judge = defaultUser
    f.jurisdiction_state = statusNA
    f.save()

if i==50:
    print('initialization success.')
else:
    print('failed on ' + str(i) + ' See above user set for details in the database.')
