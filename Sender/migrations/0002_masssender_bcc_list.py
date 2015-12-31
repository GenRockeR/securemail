# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import multi_email_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Sender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masssender',
            name='bcc_list',
            field=multi_email_field.fields.MultiEmailField(
                null=True, blank=True),
        ),
    ]
