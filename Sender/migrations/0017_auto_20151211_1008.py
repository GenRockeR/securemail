# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sender', '0016_auto_20151210_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masssender',
            name='pub_date',
            field=models.DateTimeField(
                default=datetime.datetime(
                    2015,
                    12,
                    11,
                    10,
                    8,
                    11,
                    817165),
                editable=False,
                verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438'),
        ),
    ]
