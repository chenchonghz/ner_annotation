# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0010_initialize_ner_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationresult',
            name='jurisdiction_state',
            field=models.CharField(default='PENDING', max_length=128, choices=[(b'DENIED', b'The result is denied by the adjudicator'), (b'PENDING', b'The result is not yet reviewed'), (b'ACCEPTED', b'The result is accepeted by the adjudicator')]),
            preserve_default=False,
        ),
    ]
