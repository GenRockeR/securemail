# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 08:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sender', '0004_auto_20151204_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='masssender',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(
                2015, 12, 7, 11, 35, 42, 715827), editable=False),
        ),
    ]