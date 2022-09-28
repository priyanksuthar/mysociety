from mysociety.settings import *
import dotenv
import os

ENV_PATH = os.getcwd() + '/.env'
dotenv.read_dotenv(ENV_PATH)

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('MYSQL_DB_NAME'),
        'USER': os.environ.get('MYSQL_DB_USER'),
        'PASSWORD': os.environ.get('MYSQL_DB_PASSWORD'),
        'HOST': os.environ.get('MYSQL_DB_HOST'),
        'PORT': os.environ.get('MYSQL_DB_PORT'),
    }
}

DEBUG = True if os.environ.get('DEBUG') == "True" else False

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ]
}
