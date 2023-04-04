#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # 开发环境
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cooper_django.settings')
    # dev环境配置
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cooper_django.dev_settings')
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
    # 学习视频 https://www.bilibili.com/video/BV1nf4y1k7G3?p=24
    main()
