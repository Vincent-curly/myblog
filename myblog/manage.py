#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
    """逻辑：通过读取系统环境变量中的 MYBLOG_PROFILE 来控制 Django 加载不同的 settings 文件，以此达到开发环境
    使用 develop.py 这个配置，而线上环境使用 product.py 这个配置的目的"""
    profile = os.environ.get('MYBLOG_PROFILE', 'develop')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings.%s' % profile)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
