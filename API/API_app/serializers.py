from rest_framework import serializers

from . import models

class accessoriesIDSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.ApiAppAccessoriesid
        fields = ('ARTICLE', 'CATEGORY', 'SEASON', 'BRAND', 'MATERIAL1', 'MATERIAL2', 'DESCRIPTION')

class accessoriesDetailsSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.ApiAppAccessoriesdetails
        fields = ('ARTICLE', 'COLOR', 'AGE', 'WHOLEPRICE', 'RETAILPRICE', 'INVENTORY', 'GENDER')

