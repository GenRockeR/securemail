# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
from django.contrib import admin
from django.conf import settings

# Register your models here.
from . import models
from Sender.models import MassSender
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.core.exceptions import ValidationError
from django.core import mail
from django.core.mail.message import EmailMultiAlternatives

reload(sys)
sys.setdefaultencoding('utf-8')


def make_new(ModelAdmin, request, queryset):
    """
    Устанавливаем статус рассылки - Новая
    """
    row_updated = queryset.update(status='n')
    if row_updated == 1:
        message_bit = u'1 рассылка'
    else:
        message_bit = u'%s рассылок' % row_updated
    ModelAdmin.message_user(request,
                            u'%s были помечены, как "Новые"'
                            % message_bit)
make_new.short_description = u'Пометить рассылку - "Новая"'


def make_sent(ModelAdmin, request, queryset):
    """
    Устанавливаем статус рассылки - В процессе
    """
    row_updated = queryset.update(status='p')
    if row_updated == 1:
        message_bit = u'1 рассылка'
    else:
        message_bit = u'%s рассылок' % row_updated
    ModelAdmin.message_user(request,
                            u'%s были помечены, как "В процессе"'
                            % message_bit)
make_sent.short_description = u'Пометить рассылку - "В процессе"'


def make_finished(ModelAdmin, request, queryset):
    """
    Устанавливаем статус рассылки - Завершена
    """
    row_updated = queryset.update(status='f')
    if row_updated == 1:
        message_bit = u'1 рассылка'
    else:
        message_bit = u'%s рассылок' % row_updated
    ModelAdmin.message_user(request,
                            u'%s были помечены, как "Завершенные"'
                            % message_bit)
make_finished.short_description = u'Пометить рассылку - "Завершена"'


def clean_recipients(ModelAdmin, request, queryset):
    """
    Очищаем и получаем список получателей почтовой рассылки
    Доработать получение  виде списков
    """
    if queryset.filter(status='n'):
        for mail_recipients in MassSender.bcc_list:
            mail_recipients_list = mail_recipients.strip()
            mail_recipients_list = mail_recipients.splitlines()
        return mail_recipients_list
    else:
        ModelAdmin.message_user(request, u'Ошибка обработки списка')


def get_subject(queryset):
    """
    Получаем тему сообщения для создания рассылки
    """
    mail_subject_all = queryset.all()
    for subject in mail_subject_all:
        return subject.mail_subject


def get_sender(queryset):
    """
    Получаем почтовый адрес отправителя для подстановки поддельного письма
    """
    sender_name = queryset.all()
    for name in sender_name:
        return name.sender_name.lower()


def get_body(queryset):
    """
    Получаем тело письма в формате html для создания рассылки
    """
    body_all = queryset.all()
    for body in body_all:
        return body.mailbody


def get_recipients(queryset):
    """
    Получаем список почтовых адресов пользователей для отправки
    """
    rep_list = queryset.all()
    for rep in rep_list:
        return rep.bcc_list


def get_attachment(queryset):
    """
    Получаем вложение для добавления в рассылку
    """
    attach_list = queryset.all()
    for attach in attach_list:
        # attachment = settings.MEDIA_ROOT + '/' + str(attach.mail_attachment).strip('./')
        # return attachment
        return attach.mail_attachment


def get_fullname(queryset):
    """
    Получаем имя пользователя, от которого булем отправлять рассылку
    """
    users_desc = queryset.all()
    for user_desc in users_desc:
        fullname = user_desc.sender_name_desc + \
            ' <' + user_desc.sender_name.lower() + '>'
        return fullname


def make_mail(ModelAdmin, request, queryset):
    """
    Создаем рассылку и отправляем.
    """
    from datetime import datetime
    if queryset.filter(status='n'):
        connection = mail.get_connection()
        connection.open()
        messages = list()

        for i in xrange(0, len(get_recipients(queryset))):
            rep_list = get_recipients(queryset)
            header = u'\'' + get_sender(queryset) + u'\''
            msg = EmailMultiAlternatives(
                subject = unicode(get_subject(queryset)),
                body = unicode(get_body(queryset)),
                from_email = unicode(get_fullname(queryset)),
                to = [rep_list[i]],
                # attachments=unicode(get_attachment(queryset)),
                reply_to = [unicode(get_fullname(queryset))])
            msg.attach_alternative(unicode(get_body(queryset)), 'text/html')
            # msg.attach_file(get_attachment(queryset))
            msg.attach_file(os.path.join(settings.MEDIA_ROOT, str(get_attachment(queryset))))
            msg.encoding = 'utf-8'
            messages.append(msg)
        connection.send_messages(messages)
        connection.close()
        ModelAdmin.message_user(request, u'Рассылка отправлена')
        # ModelAdmin.message_user(request, get_attachment(queryset))
        queryset.update(status='f')
        queryset.update(send_date=datetime.now())
    else:
        ModelAdmin.message_user(request,
                                u'Рассылка уже выполняется или завершена',
                                'warning')
make_mail.short_description = u'Отправить письма'


class SenderAdmin(admin.ModelAdmin):
    list_display = [
        'sender_name_desc',
        'sender_name',
        'pub_date',
        'status',
        'send_date']
    actions = [make_new, make_sent, make_finished, make_mail]
    list_filter = ['pub_date', 'send_date']
    search_fields = ['sender_name_desc']

admin.site.register(MassSender, SenderAdmin)
