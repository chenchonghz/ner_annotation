# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0004_auto_20150903_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfile',
            name='umls_comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='textfile',
            name='umls_state',
            field=models.CharField(default='NOT_READY', max_length=128, choices=[(b'NOT_READY', b'Not ready, labeling has not finished yet'), (b'IN_PROGRESS', b'In progress, assigned but not started'), (b'DIRTY', b'Started, file is dirty, but not submitted'), (b'DONE', b'Done, submitted')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='textfile',
            name='annotation_state',
            field=models.CharField(max_length=128, choices=[(b'NOT_ASSIGNED', b'Not assigned'), (b'IN_PROGRESS', b'In progress, assigned but not started'), (b'DIRTY', b'Started, file is dirty, but not submitted'), (b'DONE', b'Done, submitted')]),
        ),
        migrations.AlterField(
            model_name='textfile',
            name='jurisdiction_state',
            field=models.CharField(max_length=128, choices=[(b'NOT_ASSIGNED', b'Not assigned'), (b'IN_PROGRESS', b'In progress, assigned but not started'), (b'DIRTY', b'Started, file is dirty, but not submitted'), (b'DONE', b'Done, submitted')]),
        ),
    ]
