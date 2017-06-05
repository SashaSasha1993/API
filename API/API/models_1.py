from django.db import models
# Create your models here.
class accessoriesDetails(models.Model):
    ARTICLE = models.ForeignKey('accessoriesID'),
    COLOR = models.CharField(max_length=500),
    AGE = models.CharField(max_length=500),
    WHOLEPRICE = models.CharField(max_length=500),
    RETAILPRICE = models.CharField(max_length=500),
    INVENTORY = int,
    GENDER = models.CharField(max_length=500),

class accessoriesID(models.Model):

    ARTICLE = models.CharField(max_length=200, primary_key=True),
    CATEGORY = models.CharField(max_length=500),
    SEASON = models.CharField(max_length=500),
    BRAND = models.CharField(max_length=500),
    MATERIAL1 = models.CharField(max_length=500),
    MATERIAL2 = models.CharField(max_length=500),
    DESCRIPTION = models.CharField(max_length=500),

