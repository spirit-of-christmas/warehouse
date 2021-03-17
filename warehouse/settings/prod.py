from decouple import config
import dj_database_url

from .base import *  # noqa

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)
DATABASES = {"default": dj_database_url.config()}
