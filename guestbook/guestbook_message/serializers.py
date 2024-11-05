# guestbook_message/serializers.py
from rest_framework import serializers
from .models import GuestbookEntry


class GuestbookEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestbookEntry
        fields = ["id", "name", "message", "date"]
