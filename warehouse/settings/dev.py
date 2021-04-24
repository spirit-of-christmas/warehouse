from decouple import config

from .base import *  # noqa

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "HOST": config("POSTGRES_HOST"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "PORT": "5432",
    }
}
