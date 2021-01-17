"""
WSGI config for ms_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling # Irá fornecer os arquivos de media e static

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ms_project.settings')

application = Cling(MediaCling(get_wsgi_application()))
