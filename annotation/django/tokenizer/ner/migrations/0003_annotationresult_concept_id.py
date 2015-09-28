# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0002_textfile_annotation_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationresult',
            name='concept_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
