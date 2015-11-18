# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0007_auto_20151028_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='', blank=True, max_length=255, upload_to='tasks'),
        ),
        migrations.AddField(
            model_name='task',
            name='link_youtube',
            field=models.URLField(default='', max_length=255),
        ),
    ]
