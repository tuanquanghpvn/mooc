# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_applyforateacher'),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='teacher',
            field=models.ForeignKey(to='teachers.Teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='teacher',
            field=models.ForeignKey(to='teachers.Teacher'),
            preserve_default=False,
        ),
    ]
