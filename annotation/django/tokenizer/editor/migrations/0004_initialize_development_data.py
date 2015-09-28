# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User,Group
from django.db import models, migrations


class Migration(migrations.Migration):

    def initialize_development_data(apps, schema_editor):
        User.objects.create_user(username='test', password='test')

        Group.objects.create(name='tokenization_annotator')
        Group.objects.create(name='tokenization_adjudicator')

        Status = apps.get_model("editor", "Status")
        TextFile = apps.get_model("editor", "TextFile")

        Status.objects.create(state_text='NA')
        Status.objects.create(state_text='IN')
        Status.objects.create(state_text='DONE')
        Status.objects.create(state_text='DIRTY')

        TextFile.objects.create(file_name='A 00 (1).txt', file_location='editor/data/original/A 00 (1).txt', first_worker_id=1, first_worker_state_id=1, first_worker_comment='', second_worker_id=1, second_worker_state_id=1, second_worker_comment='', judge_id=1, jurisdiction_state_id=1)

    dependencies = [
        ('editor', '0003_auto_20150803_0346'),
    ]

    operations = [
        migrations.RunPython(initialize_development_data),
    ]
