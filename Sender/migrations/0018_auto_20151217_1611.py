# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 13:11
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import multi_email_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sender', '0017_auto_20151211_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='masssender',
            options={
                'verbose_name': '\u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0443',
                'verbose_name_plural': '\u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438'},
        ),
        migrations.AddField(
            model_name='masssender',
            name='sender_name_desc',
            field=models.CharField(
                max_length=100,
                null=True,
                verbose_name='\u0418\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f'),
        ),
        migrations.AlterField(
            model_name='masssender',
            name='bcc_list',
            field=multi_email_field.fields.MultiEmailField(
                help_text='\u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u0441\u043f\u0438\u0441\u043e\u043a \u0434\u043b\u044f \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438 \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443 \u0430\u0434\u0440\u0435\u0441\u0443 \u0432 \u0441\u0442\u0440\u043e\u043a\u0435',
                null=True,
                verbose_name='\u041a\u043e\u043c\u0443:'),
        ),
        migrations.AlterField(
            model_name='masssender',
            name='mailbody',
            field=ckeditor.fields.RichTextField(
                verbose_name='\u0422\u0435\u043b\u043e \u043f\u0438\u0441\u044c\u043c\u0430'),
        ),
        migrations.AlterField(
            model_name='masssender',
            name='pub_date',
            field=models.DateTimeField(
                default=datetime.datetime(
                    2015,
                    12,
                    17,
                    16,
                    11,
                    50,
                    509563),
                editable=False,
                verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438'),
        ),
    ]
