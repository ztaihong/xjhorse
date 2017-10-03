"""
WSGI config for xjhorse project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling                                             # 处理静态文件的第三方包

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xjhorse.settings")     # 缺省的项目设置文件

application = Cling(get_wsgi_application())                             # 处理静态文件
