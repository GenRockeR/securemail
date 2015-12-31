# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.shortcuts import HttpResponse


def index(request):
    html = '<H1>People</H1><HR>'
    return HttpResponse(html)
