"""
Django settings for SecureMail project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+uzw)7y1@&e9u$+z3ebk0!0t2*zz&ry7@!+1@&b#n3etwnt5qe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEFAULT_CHARSET = 'utf-8'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Sender',
    'django.contrib.admin',
    'sorl.thumbnail',
    'ckeditor',
    'favicon',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'SecureMail.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/var/www/html/SecureMail/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SecureMail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'securemail',
        'USER': 'root',
        'PASSWORD': '4eLOve4iwe4e',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_ENGINE = 'redis_sessions.session'
# SESSION_REDIS_PASSWORD = 'password'
# SESSION_REDIS_PREFIX = 'session'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

# LANGUAGES = (
#   ( 'Ru', 'Russian')
# )

TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = '/var/www/html/SecureMail/Uploads'
STATIC_ROOT = '/var/www/html/SecureMail/static'

CKEDITOR_JQUERY_URL = 'static/jquery-2.1.4.min.js'
CKEDITOR_UPLOAD_PATH = 'Uploads/images/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Full': [
            ['Styles',
             'Format',
             'Font',
             'FontSize',
             'Bold',
             'Italic',
             'Underline',
             'Strike',
             'Subscript',
             'Superscript',
             '-',
             'RemoveFormat'],
            ['Image', 'Table', 'SpecialChar', 'Smiley'],
            ['TextColor', 'BGColor'],
            ['Link', 'Unlink', 'Anchor'],
            ['NumberedList',
             'BulletedList',
             '-',
             'Outdent',
             'Indent',
             '-',
             'Blockquote',
             '-',
             'JustifyLeft',
             'JustifyCenter',
             'JustifyRight',
             'JustifyBlock',
             '-',
             'BidiLtr',
             'BidiRtl',
             'Language'],
            ['Cut', 'Copy', 'Paste', 'PasteText',
                'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll'],
        ],
        'height': '480',
        'width': '100%',
        'removePlugins': 'resize',
    },
}

PYMORPHY_DICTS = {
    'ru': {'dir': '/var/www/html/SecureMail/dicts'},
}

LOCALE_PATHS = (PROJECT_ROOT + '/locale', )
FAVICON_PATH = STATIC_URL + 'images/favicon.png'

EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'

# EMAIL_HOST = '10.1.2.19'
# EMAIL_PORT = '25'

# DEFAULT_FILE_STORAGE = 'utils.storage.ASCIIFileSystemStorage'