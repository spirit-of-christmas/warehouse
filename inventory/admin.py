from django.contrib import admin
from . import models

admin.site.register(models.Location)
admin.site.register(models.Department)
admin.site.register(models.Category)
admin.site.register(models.Quality)
admin.site.register(models.Product)
