# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_applyforateacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(default='', blank=True)),
                ('num_question', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('image', models.ImageField(default='', upload_to='exams', max_length=255)),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(default='', blank=True)),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=255)),
                ('level', models.IntegerField(default=1, choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')])),
                ('type', models.IntegerField(default=1, choices=[(1, 'One choice'), (2, 'Multiple choice')])),
                ('group', models.ForeignKey(to='exams.Group')),
                ('teacher', models.ForeignKey(to='teachers.Teacher')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='group',
            field=models.ForeignKey(to='exams.Group'),
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher',
            field=models.ForeignKey(to='teachers.Teacher'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='exams.Question', related_name='answers'),
        ),
    ]
