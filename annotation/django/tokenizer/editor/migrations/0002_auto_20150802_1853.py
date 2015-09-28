# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfile',
            name='first_worker_comment',
            field=models.CharField(max_length=1000, default=datetime.datetime(2015, 8, 2, 18, 52, 33, 503127, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textfile',
            name='second_worker_comment',
            field=models.CharField(max_length=1000, default='no comment'),
            preserve_default=False,
        ),
    ]
