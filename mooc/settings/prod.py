from mooc.settings.base import *

DEBUG = False

THIRD_APPS = [
        'django_extensions',
]

INSTALLED_APPS += THIRD_APPS

ALLOWED_HOSTS = ['*']