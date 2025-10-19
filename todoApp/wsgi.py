"""
WSGI config for todoApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todoApp.settings")

# This line ensures Django is fully initialized
application = get_wsgi_application()

# Run collectstatic after Django is initialized
if os.environ.get('VERCEL_ENV') == 'production':
    call_command('collectstatic', '--noinput')

# Expose the application for Vercel
app = application