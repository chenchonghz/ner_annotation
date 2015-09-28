# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0003_annotationresult_concept_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='annotation_state',
            field=models.CharField(max_length=128, choices=[(b'NOT_ASSIGNED', b'Not assigned'), (b'IN_PROGRESS', b'In progress, assigned but not started'), (b'DONE', b'Done, submitted'), (b'DIRTY', b'Started, file is dirty, but not submitted')]),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='jurisdiction_state',
            field=models.CharField(max_length=128, choices=[(b'NOT_ASSIGNED', b'Not assigned'), (b'IN_PROGRESS', b'In progress, assigned but not started'), (b'DONE', b'Done, submitted'), (b'DIRTY', b'Started, file is dirty, but not submitted')]),
        ),
    ]
