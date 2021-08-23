from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_site',
<<<<<<< HEAD
        'USER': '',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
    
=======
        'USER': 'root',
        'PASSWORD':'Alexix31',
        'HOST':'localhost',
        'PORT':'3306',
        
>>>>>>> parent of 07800df ( - agregué settings/local a .gitignore para que no se guarden las configuraciones de base de datos de cada uno (se veia la contraseña de root))
    }
}