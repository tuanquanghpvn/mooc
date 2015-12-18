# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20151218_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='code',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]
