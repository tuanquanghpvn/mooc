# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='info',
            field=models.TextField(default='', blank=True),
        ),
    ]
