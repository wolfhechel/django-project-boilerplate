from ._pre_config import PROJECT_ROOT, path

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(PROJECT_ROOT, 'development.db')
    }
}
