from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
print(f'ALLOWED_HOSTS = {ALLOWED_HOSTS}')

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        # para trabajar con postgressql
#        # hay que instalar en el entorno virtual pip install pysql
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'schollar_transpro',
#        'USER': 'transporte',
#        'PASSWORD': 'parada2023',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'schollar_transpro'),
        'USER': os.environ.get('DB_USER', 'transporte'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'parada2023'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'