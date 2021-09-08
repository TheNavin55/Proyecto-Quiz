# production.py
from .base import *
DEBUG = False
ALLOWED_HOSTS = ['informatorio-grupo-1-2021.herokuapp.com/', '127.0.0.1/']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = 'https://informatorio-grupo-1-2021.herokuapp.com/'
MEDIA_URL = 'https://informatorio-grupo-1-2021.herokuapp.com//'