from django.db import models
from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from taggit.managers import TaggableManager


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quality(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")

    def __str__(self):
        return self.title


class StockItem(models.Model):
    GENDERS = [("male", "Male"), ("female", "Female"), ("both", "Both")]

    title = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.title
