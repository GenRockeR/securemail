# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 08:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sender', '0008_auto_20151207_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masssender',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(
                2015, 12, 7, 11, 44, 25, 202137), editable=False),
        ),
        migrations.AlterField(
            model_name='masssender',
            name='sender_name',
            field=models.EmailField(
                max_length=50,
                verbose_name='\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043e\u0442'),
        ),
    ]
