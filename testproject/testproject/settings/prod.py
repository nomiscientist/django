from testproject.settings.base import *

# override base.py settings here


try:
    from testproject.settings.local import *
except:
    pass


DEBUG = False

ALLOWED_HOSTS = ['172.16.4.136']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# SQLIT# NOT RECOMMENDEDDDD FOR PRODUCTION ENV

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
