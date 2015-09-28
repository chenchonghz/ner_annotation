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
            name='AnnotationResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token_text', models.CharField(max_length=50)),
                ('start_position', models.IntegerField()),
                ('end_position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TextFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.CharField(max_length=50)),
                ('file_location', models.CharField(max_length=200)),
                ('annotation_state', models.CharField(max_length=2, choices=[(b'NOT_ASSIGNED', b'Not assigned'), (b'IN_PROGRESS', b'In progress, assigned but not started'), (b'DONE', b'Done, submitted'), (b'DIRTY', b'Started, file is dirty, but not submitted')])),
                ('jurisdiction_state', models.CharField(max_length=2, choices=[(b'NOT_ASSIGNED', b'Not assigned'), (b'IN_PROGRESS', b'In progress, assigned but not started'), (b'DONE', b'Done, submitted'), (b'DIRTY', b'Started, file is dirty, but not submitted')])),
                ('file_content', models.TextField(blank=True)),
                ('adjudicator', models.ForeignKey(related_name='adjudicator', to=settings.AUTH_USER_MODEL)),
                ('annotator', models.ForeignKey(related_name='annotator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='annotationresult',
            name='category',
            field=models.ForeignKey(related_name='category', to='ner.Category'),
        ),
        migrations.AddField(
            model_name='annotationresult',
            name='text_file',
            field=models.ForeignKey(related_name='text_file', to='ner.TextFile'),
        ),
    ]
