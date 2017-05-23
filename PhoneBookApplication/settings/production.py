import dj_database_url
from .base import DATABASES

DEBUG = True  # Why persecute me heroku???
ALLOWED_HOSTS = ['app-phonebook.herokuapp.com', ]

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'