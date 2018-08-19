# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=1024)),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 8, 48, 19, 219216))),
            ],
        ),
        migrations.CreateModel(
            name='Downvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 8, 48, 19, 222625))),
                ('answer', models.ForeignKey(to='feed_models.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.CharField(max_length=1024)),
                ('username', models.CharField(max_length=128)),
                ('views', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 8, 48, 19, 220289))),
                ('answers', models.ManyToManyField(related_name='answers_for_question', to='feed_models.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 8, 48, 19, 218577))),
            ],
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 8, 18, 8, 48, 19, 222039))),
                ('answer', models.ForeignKey(to='feed_models.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(to='feed_models.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='feed_models.Question'),
        ),
    ]
