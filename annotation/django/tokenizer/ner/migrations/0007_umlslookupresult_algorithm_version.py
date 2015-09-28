# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0006_umlslookupresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='umlslookupresult',
            name='algorithm_version',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
