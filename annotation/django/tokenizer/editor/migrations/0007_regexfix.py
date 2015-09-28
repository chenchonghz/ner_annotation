# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0006_textfile_file_content_original'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegexFix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pattern', models.CharField(max_length=200)),
                ('replacement', models.CharField(max_length=200)),
            ],
        ),
    ]
