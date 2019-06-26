"""
Django project settings for the production environment.
"""
from .base import * # noqa
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env('../../.env')

TEST=env.ENVIRON

env = environ.Env(
    AWS_ACCESS_KEY_ID=(str, False),
    AWS_SECRET_ACCESS_KEY=(str, False),
    AWS_STORAGE_BUCKET_NAME=(str, False))
environ.Env.read_env('/var/www/ig_photos/.env')

DEBUG = True

ALLOWED_HOSTS = [
    '*'
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

INSTALLED_APPS = INSTALLED_APPS + ['storages',]

# # default django-storages settings
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# AWS_S3_REGION_NAME = os.getenv('AWS_REGION_NAME')
# AWS_AUTO_CREATE_BUCKET = True
#
# # S3 BUCKET STUFF GOES HERE
# AWS_STATIC_BUCKET_NAME = 'rtk-static'
# AWS_STATIC_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STATIC_BUCKET_NAME
# STATIC_URL = "https://%s/" % AWS_STATIC_CUSTOM_DOMAIN
# STATICFILES_STORAGE = 'config.settings.storage_backends.StaticStorage'
#
# # django-storages settings for all other files (including data files)
# AWS_STORAGE_BUCKET_NAME = 'rtk-data'
# AWS_DEFAULT_ACL = 'private'
# AWS_BUCKET_ACL = 'private'
#
# # Same idea as data location in local.py
# DATA_LOCATION = 'rmp'

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENCRYPTION = True
#AWS_AUTO_CREATE_BUCKET = True
#AWS_DEFAULT_ACL = 'public-read'
#AWS_BUCKET_ACL = 'public-read'

AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
#AWS_S3_OBJECT_PARAMETERS = {'CacheContro': 'max-age=86400'}

STATIC_LOCATION = 'static'
STATIC_URL='/ig-photos/static/'
#STATICFILES_STORAGE = 'config.settings.storage_backends.StaticStorage'

PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = 'news/projects-staging/ig-photos/media/'
DEFAULT_FILE_STORAGE = 'config.settings.storage_backends.MediaStorage'
