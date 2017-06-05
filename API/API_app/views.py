from . import models
from rest_framework import generics
from . import serializers

# Create your views here.


class ListCreateAccessoriesID(generics.ListCreateAPIView):
    queryset = models.ApiAppAccessoriesid.objects.all()
    serializer_class =serializers.accessoriesIDSerializer

class ListCreateAccessoriesDetails(generics.ListCreateAPIView):
    queryset = models.ApiAppAccessoriesdetails.objects.all()
    serializer_class =serializers.accessoriesDetailsSerializer