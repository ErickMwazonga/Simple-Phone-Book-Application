"""
WSGI config for PhoneBookApplication project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PhoneBookApplication.settings")
#
# application = get_wsgi_application()
#

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

path = '/home/erick/apps/PhoneBookApplication/'
if path not in sys.path:
    sys.path.append(path)

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PhoneBookApplication.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "PhoneBookApplication.settings"

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
