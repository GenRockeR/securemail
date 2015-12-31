# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from multi_email_field.fields import MultiEmailField
from datetime import datetime
from .validators import validate_file_extension
from .storages import OverwriteStorage

STATUS_CHOICES = (
    ('n', u'Новaя'),
    ('p', u'В процессе'),
    ('f', u'Завершена'),
)


class MassSender(models.Model):

    class Meta:
        verbose_name = u'рассылку'
        verbose_name_plural = u'рассылки'

    sender_name_desc = models.CharField(
        u'Имя отправителя', max_length=100, null=True)
    sender_name = models.EmailField(u'Отправить от', max_length=50)
    bcc_list = MultiEmailField(u'Кому:', null=True,
                               help_text=u'Добавьте список для рассылки по одному адресу в строке')
    mail_subject = models.CharField(u'Тема письма', max_length=200, null=True)
    mailbody = RichTextField(u'Тело письма')
    mail_attachment = models.FileField(
        u'Вложение',
        validators=[validate_file_extension],
        storage=OverwriteStorage())
    pub_date = models.DateTimeField(
        u'Дата добавления рассылки',
        editable=False,
        default=datetime.now())
    status = models.CharField(
        u'Статус рассылки',
        max_length=1,
        choices=STATUS_CHOICES,
        editable=False,
        default='n')
    send_date = models.DateTimeField(
        u'Дата отправки рассылки',
        editable=False,
        blank=True,
        null=True)


    def __unicode__(self):
        return self.sender_name
