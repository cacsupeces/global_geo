# https://docs.djangoproject.com/en/1.8/topics/settings/
# https://docs.djangoproject.com/en/1.8/ref/settings/


from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '49$8993!fae5wf-1^!sam*-2h$#6kv)di$c0tv(el-q^pgy-_@'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Caches
# https://docs.djangoproject.com/en/1.8/topics/cache/#local-memory-caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
CACHE_MIDDLEWARE_ALIAS = 'default'


# Email
# https://docs.djangoproject.com/en/1.8/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
