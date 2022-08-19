from webpush import send_user_notification
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET


# @require_GET
# @csrf_exempt
def index(request):
    user = request.user
    payload = {"head": "Welcome!", "body": "Hello World"}
    send_user_notification(user=user, payload=payload, ttl=1000)
    return render(request, 'index.html')



# from myproject.profiles.models import Profile


# class UpdateLastActivityMiddleware(object):
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         assert hasattr(request, 'user'), 'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'
#         if request.user.is_authenticated():
#             Profile.objects.filter(user__id=request.user.id) \
#                            .update(last_activity=timezone.now())
