# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_applyforateacher'),
        ('categories', '0001_initial'),
        ('subjects', '0009_remove_task_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(default='', blank=True)),
                ('num_question', models.IntegerField()),
                ('category', models.ForeignKey(to='categories.Category')),
                ('subject', models.ForeignKey(to='subjects.Subject')),
                ('teacher', models.ForeignKey(to='teachers.Teacher')),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='categories.Category')),
                ('teacher', models.ForeignKey(to='teachers.Teacher')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='exams.Question', related_name='answers'),
        ),
    ]
