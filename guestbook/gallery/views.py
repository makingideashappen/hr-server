from django.shortcuts import render
from .models import Photo
from .serializers import PhotoSerializer
from rest_framework import generics

# Create your views here.


class PhotoListView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
