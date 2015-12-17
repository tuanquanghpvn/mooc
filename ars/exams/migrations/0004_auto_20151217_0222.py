# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_exam_minute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='minute',
            field=models.IntegerField(),
        ),
    ]
