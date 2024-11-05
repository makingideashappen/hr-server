from .views import PhotoListView
from django.urls import path

urlpatterns = [
    path("", PhotoListView.as_view(), name="photo_files"),
]
