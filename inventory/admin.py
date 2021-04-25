from django.contrib import admin
from . import models

admin.site.register(models.Department)
admin.site.register(models.Type)
admin.site.register(models.Quality)
admin.site.register(models.StockItem)
