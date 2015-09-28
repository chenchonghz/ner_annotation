# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfile',
            name='annotation_comment',
            field=models.TextField(blank=True),
        ),
    ]
