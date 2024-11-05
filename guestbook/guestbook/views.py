# guestbook/views.py

from django.http import JsonResponse
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


def new_captcha(request):
    captcha_key = CaptchaStore.generate_key()
    image_url = captcha_image_url(captcha_key)
    return JsonResponse({"key": captcha_key, "image_url": image_url})
