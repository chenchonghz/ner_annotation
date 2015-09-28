# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_auto_20150802_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='first_worker_comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='second_worker_comment',
            field=models.TextField(blank=True),
        ),
    ]
