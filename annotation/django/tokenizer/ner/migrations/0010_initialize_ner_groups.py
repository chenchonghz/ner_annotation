# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Group
from django.db import models, migrations


class Migration(migrations.Migration):

    def initialize_ner_groups(apps, schema_editor):
        Group.objects.create(name='ner_annotator')
        Group.objects.create(name='ner_adjudicator')

    dependencies = [
        ('ner', '0009_auto_20150904_2135'),
    ]

    operations = [
        migrations.RunPython(initialize_ner_groups),
    ]
