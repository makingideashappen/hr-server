# forms.py
from django import forms
from captcha.fields import CaptchaField
from .models import GuestbookEntry


class GuestbookEntryForm(forms.ModelForm):
    captcha = CaptchaField()  # Add CAPTCHA field to form

    class Meta:
        model = GuestbookEntry
        fields = ["name", "message"]


class GuestbookForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
