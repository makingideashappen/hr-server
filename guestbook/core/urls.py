from django.urls import path
from .views import GuestBookEntryListCreate

urlpatterns = [
    path("entries/", GuestBookEntryListCreate.as_view(), name="guestbook-entries"),
]
