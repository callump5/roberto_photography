from base import *
import dj_database_url

DEBUG = False


DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}


AWS_ACCESS_KEY_ID = os.getenv('AWS_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_KEY')



# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}