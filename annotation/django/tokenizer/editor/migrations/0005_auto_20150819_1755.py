# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_initialize_development_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfile',
            name='file_content1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='textfile',
            name='file_content2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='textfile',
            name='file_content_final',
            field=models.TextField(blank=True),
        ),
    ]
