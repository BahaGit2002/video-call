from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home),
    # path('sendpush/', views.send_push, name='sendpush'),
    # path('home/', views.home, name='home')
]
