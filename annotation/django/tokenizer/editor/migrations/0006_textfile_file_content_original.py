# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0005_auto_20150819_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfile',
            name='file_content_original',
            field=models.TextField(blank=True),
        ),
    ]
