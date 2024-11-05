# guestbook_message/urls.py
from django.urls import path
from .views import GuestbookEntryList, add_entry

urlpatterns = [
    path("entries/", GuestbookEntryList.as_view(), name="guestbook-entry-list"),
    path("add/", add_entry, name="guestbook-entry-list"),
]
