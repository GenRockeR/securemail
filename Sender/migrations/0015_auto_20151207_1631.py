# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 13:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sender', '0014_auto_20151207_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masssender',
            old_name='mail_theme',
            new_name='mail_subject',
        ),
        migrations.AlterField(
            model_name='masssender',
            name='pub_date',
            field=models.DateTimeField(
                default=datetime.datetime(
                    2015,
                    12,
                    7,
                    16,
                    31,
                    35,
                    28402),
                editable=False,
                verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='masssender',
            name='status',
            field=models.CharField(
                choices=[
                    (b'n',
                     '\u041d\u043e\u0432a\u044f'),
                    (b'p',
                     '\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435'),
                    (b'f',
                     '\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0430')],
                default=b'n',
                editable=False,
                max_length=1,
                verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438'),
        ),
    ]