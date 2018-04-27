from testproject.settings.base import *

# override base.py settings here

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases




try:
    from testproject.settings.local import *
except:
    pass


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}