# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Group
from django.db import models, migrations


class Migration(migrations.Migration):

    def initialize_admin_group(apps, schema_editor):
        Group.objects.create(name='editor_admin')

    dependencies = [
        ('editor', '0007_regexfix'),
    ]

    operations = [
        migrations.RunPython(initialize_admin_group),
    ]
