# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0005_auto_20150903_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='UmlsLookupResult',
            fields=[
                ('source', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('result', models.TextField(blank=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
