"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
"""逻辑：通过读取系统环境变量中的 MYBLOG_PROFILE 来控制 Django 加载不同的 settings 文件，以此达到开发环境
    使用 develop.py 这个配置，而线上环境使用 product.py 这个配置的目的"""
profile = os.environ.get('MYBLOG_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings.%s' % profile)

application = get_wsgi_application()
