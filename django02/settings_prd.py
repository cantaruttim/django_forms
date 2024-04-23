import os

ENVIRONMENT = os.getenv('ENVIRONMENT')
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DATABASE'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
        'OPTIONS': {
            'sslmode': os.getenv('POSTGRES_SSL_MODE'),
            'options': os.getenv('POSTGRES_OPTIONS')
        }
    }
}