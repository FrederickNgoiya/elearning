# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-13 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0008_auto_20190531_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='color',
            field=models.CharField(default='#007bff', max_length=7),
        ),
    ]
