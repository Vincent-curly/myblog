# flake8: NOQA

from .base import *


DEBUG = True        # 开发环境使用

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}