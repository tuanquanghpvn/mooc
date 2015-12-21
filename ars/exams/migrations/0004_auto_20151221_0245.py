# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20151218_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='fill',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exam',
            name='level',
            field=models.IntegerField(choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3')], default=1),
        ),
    ]
