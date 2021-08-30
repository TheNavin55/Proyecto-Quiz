from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_site',
        'USER': 'root',
        'PASSWORD':'Alexix31',
        'HOST':'',
        'PORT':'3306',

    }
}