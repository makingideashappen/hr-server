# guestbook_message/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GuestbookEntry
from .serializers import GuestbookEntrySerializer
from .forms import GuestbookForm
from django.shortcuts import render, redirect


class GuestbookEntryList(APIView):
    def get(self, request):
        entries = GuestbookEntry.objects.all()
        serializer = GuestbookEntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestbookEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # views.py


def add_entry(request):
    if request.method == "POST":
        form = GuestbookForm(request.POST)
        if form.is_valid():
            # Process the valid form and save the entry
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            # Save to DB
            return redirect("guestbook")  # Redirect to a success page
    else:
        form = GuestbookForm()
    return render(request, "guestbook.html", {"form": form})
