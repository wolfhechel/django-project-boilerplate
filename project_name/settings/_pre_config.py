from os import path

try:
    from .database import DATABASES
except ImportError:
    print 'No database has been configured, disabling database support'
    DATABASES = {}

    if 'south' in INSTALLED_APPS:
        INSTALLED_APPS = tuple([x for x in INSTALLED_APPS if x is not 'south'])

from os import path

SETTINGS_ROOT = path.abspath(path.dirname(__file__))
PROJECT_ROOT = path.abspath(path.join(SETTINGS_ROOT, '..'))

root = lambda *a: path.abspath(path.join(PROJECT_ROOT, *a))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = root('..', 'public_html', 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = root('..', 'public_html', 'static')

_SECRET_KEY_PATH = path.join(SETTINGS_ROOT, 'secret_key.py')
if not path.exists(_SECRET_KEY_PATH):
    from django.utils.crypto import get_random_string

    allowed_chars = 'abcdefghipqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(50, allowed_chars)

    with open(_SECRET_KEY_PATH, 'w') as _file:
        _file.write("SECRET_KEY = '%i'\n" % secret_key)

from secret_key import SECRET_KEY
