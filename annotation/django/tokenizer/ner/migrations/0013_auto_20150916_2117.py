# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0012_auto_20150916_0155'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='annotationresult',
            index_together=set([('start_position', 'end_position')]),
        ),
    ]
