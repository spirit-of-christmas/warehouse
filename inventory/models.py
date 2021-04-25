from django.core.files.base import ContentFile
from django.db import models
from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from taggit.managers import TaggableManager

from .barcodes import BarCode


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quality(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")

    def __str__(self):
        return self.title


class Product(models.Model):
    GENDERS = [("male", "Male"), ("female", "Female"), ("both", "Both")]

    title = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, choices=GENDERS)
    tags = TaggableManager()
    age_range = IntegerRangeField(
        default="(1, 18)",
        validators=[
            RangeMinValueValidator(1),
            RangeMaxValueValidator(18),
        ]
    )
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    barcode_id = models.BigIntegerField(default=0)
    barcode = models.ImageField(upload_to="barcodes/", default='default.png')

    def __str__(self):
        return self.title

    def generate_barcode(self):
        barcode = BarCode(self.barcode_id)
        self.barcode.save(f"/barcodes/{self.barcode_id}.gif", ContentFile(barcode.asString("gif")), save=False)

    def save(self, *args, **kwargs):
        self.generate_barcode()
        super(Product, self).save(*args, **kwargs)
