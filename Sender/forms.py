# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from multi_email_field.forms import MultiEmailField


class SendMessageForm(forms.Form):
    emails = MultiEmailField()
