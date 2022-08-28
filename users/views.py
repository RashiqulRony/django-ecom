from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User
from .form import UserValidation


def login(request):
    return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        form = UserValidation(request.POST)
        try:
            if form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')

                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exists')
                    return redirect('/users/register')

                if password != confirm_password:
                    messages.error(request, 'Confirm password dose not match')
                    return redirect('/users/register')

                User.objects.create(
                    name=name,
                    email=email,
                    password=make_password(password),
                    is_active=True,
                    status=True,
                )
                messages.success(request, 'User register successfully. Please Login')
                return redirect('/users/login')

            return render(request, 'users/register.html')

        except ObjectDoesNotExist:
            messages.error(request, 'Something went wrong')
            return redirect('/users/register')

    return render(request, 'users/register.html')
