from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
    vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
    print(vapid_key)
    user = request.user
    payload = {'head': 'hello', 'body': 'ыолтаоф'}
    send_user_notification(user=user, payload=payload, ttl=1000)
    return render(request, 'index.html', {user: user, 'vapid_key': vapid_key})


def home(request):
    return render(request, 'home.html')
#
# @require_POST
# @csrf_exempt
# def send_push(request):
#     if request.method == "get":
#         user = User.objects.all()
#         return render(request, 'home.html', {'user': user})
#     if request.method == "POST":
#         # print(request.POST['head'])
#         try:
#             data = {}
#             data['body'] = request.POST.get('body')
#             data['head'] = request.POST.get('head')
#             # if 'head' not in data or 'body' not in data or 'id' not in data:
#             #     return JsonResponse(status=400, data={"message": "Invalid data format"})
#             print(request.POST)
#
#
#             return JsonResponse(status=200, data={"message": "Web push successful"})
#         except TypeError:
#             return JsonResponse(status=500, data={"message": "An error occurred"})

