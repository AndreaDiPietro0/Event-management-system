"""
WSGI config for Event_management_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

# Set default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Event_management_system.settings")

# Set up Django
import django
django.setup()

# Create WSGI application
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

app = application
