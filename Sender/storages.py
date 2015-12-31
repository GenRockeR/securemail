# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import unicodedata
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        """
        Перезаписываем файлы, щагруженные в процессе создания рассылок.
        """
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


#    def get_valid_name(self, name):
#        """
#        Конвертация имен файлов в ASCII символы.
#        """
#        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
#        return super(OverwriteStorage, self).get_valid_name(name)
