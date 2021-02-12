from .base import *

DEBUG = False

ALLOWED_HOSTS = ['msat.herokuapp.com',]

SECURE_SSL_REDIRECT = True

STATIC_URL = 'https://{0}/{1}/'.format(
    AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

