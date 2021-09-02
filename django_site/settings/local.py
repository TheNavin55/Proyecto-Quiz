from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_site',
<<<<<<< Updated upstream
        'USER': 'roottest',
        'PASSWORD':'',
        'HOST':'localhost',
=======
        'USER': 'root',
        'PASSWORD':'nico123',
        'HOST':'',
>>>>>>> Stashed changes
        'PORT':'3306',

    }
}