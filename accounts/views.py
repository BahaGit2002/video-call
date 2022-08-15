from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegisterForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = RegisterForm()
        return render(request, 'register.html')
