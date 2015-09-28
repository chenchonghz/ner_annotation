# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0007_umlslookupresult_algorithm_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationresult',
            name='umls_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
