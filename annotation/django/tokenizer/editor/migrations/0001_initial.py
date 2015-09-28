# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('state_text', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TextFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('file_name', models.CharField(max_length=50)),
                ('file_location', models.CharField(max_length=200)),
                ('first_worker', models.ForeignKey(related_name='first_worker', to=settings.AUTH_USER_MODEL)),
                ('first_worker_state', models.ForeignKey(related_name='first_worker_state', to='editor.Status')),
                ('judge', models.ForeignKey(related_name='judge', to=settings.AUTH_USER_MODEL)),
                ('jurisdiction_state', models.ForeignKey(related_name='jurisdiction_state', to='editor.Status')),
                ('second_worker', models.ForeignKey(related_name='second_worker', to=settings.AUTH_USER_MODEL)),
                ('second_worker_state', models.ForeignKey(related_name='second_worker_state', to='editor.Status')),
            ],
        ),
    ]
