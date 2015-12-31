# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError


def validate_file_extension(value):
    """
    Определяем, какой тип файлов и их расширений мы можем использовать при загрузке
    файлов во вложении письма.
    Переписать потом на проверку типа файла, а не по расширению.
    """
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [
        '.pdf',
        '.doc',
        '.docx',
        '.jpg',
        '.png',
        '.xlsx',
        '.xls']
    if not ext in valid_extensions:
        raise ValidationError(
            u'Запрещенное вложение. Поддерживаются только файлы картинок и документов')
