# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 08:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sender', '0006_auto_20151207_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masssender',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(
                2015, 12, 7, 11, 42, 37, 643390), editable=False),
        ),
    ]
