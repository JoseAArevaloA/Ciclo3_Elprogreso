from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ecommerce-elprogreso.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5684eshaufv8b',
        'USER': 'snkfnlgruqpcip',
        'PASSWORD': 'c7f3a58a9bb6d196dda0833e4a1c49528f1b5c03934e60c047fe90c01173b8db',
        'HOST': 'ec2-18-209-78-11.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}
