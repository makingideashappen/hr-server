from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list_files, name="list_files"),
    path("download/<str:filename>/", views.download_file, name="download_file"),
    path("upload/", views.upload_file, name="upload_file"),
]
