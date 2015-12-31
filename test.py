# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Sender.models import MassSender
from django.db import models
import .manage

# Create your models here.
from ckeditor.fields import RichTextField
from multi_email_field.fields import MultiEmailField
from datetime import datetime
from .validators import validate_file_extension
from .storages import OverwriteStorage


p = MassSender.objects.all().values("bcc_list").filter(status='n')
print p
