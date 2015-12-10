# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('subjects', '0009_remove_task_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=255)),
                ('correct', models.BooleanField()),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(default='', blank=True)),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='categories.Category')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(related_name='exams', db_table='exam_question', to='exams.Question'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='exams.Question'),
        ),
    ]
