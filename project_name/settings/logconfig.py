import logging
import sys

def debug_to_info(record):
    return record.levelno < logging.WARNING

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'debug_to_info': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': debug_to_info,
        }
    },

    'handlers': {
        'stderr': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'stream': sys.stderr,
            'formatter': 'verbose'
        },
        'stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },

    'loggers': {
        'django': {
            'handlers': ['stderr', 'stdout'],
        },
        'django.db.backends': {
            'handlers': ['mail_admins', 'stderr'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins', 'stderr'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins', 'stderr'],
            'level': 'WARNING',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['stderr', 'stdout'],
        },
    }
}