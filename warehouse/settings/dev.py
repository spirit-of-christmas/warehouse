from decouple import config

from .base import *  # noqa

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
