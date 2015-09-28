# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0008_annotationresult_umls_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationresult',
            name='umls_id',
            field=models.TextField(blank=True),
        ),
    ]
