from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("last_name", "first_name", "username", "email", "password", "password2")

    # def save(self, commit=True):
    #     user = User.objects.create_user()

