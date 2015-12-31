# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MassSender',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.EmailField(max_length=30)),
                ('mailbody', tinymce.models.HTMLField()),
                ('mail_attachment', models.FileField(upload_to=b'')),
            ],
        ),
    ]
