# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_exam_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='minute',
            field=models.IntegerField(default=0),
        ),
    ]
