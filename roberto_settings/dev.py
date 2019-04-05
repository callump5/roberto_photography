from base import *

from aws_login import AWS_SECRET_ACCESS_KEY as SAK
from aws_login import AWS_ACCESS_KEY_ID as AAK


DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AWS_ACCESS_KEY_ID = AAK
AWS_SECRET_ACCESS_KEY = SAK