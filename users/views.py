from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as access_login, logout
from django.contrib import messages

from .middleware import is_login
from .models import User, Vendor, Customer
from .form import UserValidation


def login(request):
    if request.user.is_authenticated:
        print("You are already logged in")
        return redirect("users:dashboard")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            check_user = User.objects.get(username=username, is_active=1, is_superuser=0)
        except Exception as e:
            print(e)
            check_user = None

        if check_user:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                access_login(request, user)
                return redirect('users:dashboard')
            else:
                messages.error(request, 'Invalid username and password')
                return render(request, 'users/login.html')
        else:
            messages.error(request, "You're not user. Please Signup first.")
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')


def register(request):
    if request.user.is_authenticated:
        print("You are already logged in")
        return redirect("users:dashboard")

    if request.method == 'POST':
        form = UserValidation(request.POST)
        try:
            if form.is_valid():
                username = request.POST.get('username')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')
                user_type = request.POST.get('user_type')

                if user_type == 'vendor':
                    vendor = True
                    if Vendor.objects.filter(phone=phone).exists():
                        messages.error(request, 'This phone number already exists')
                        return redirect('/users/register')
                else:
                    vendor = False

                if user_type == 'customer':
                    customer = True
                    if Customer.objects.filter(phone=phone).exists():
                        messages.error(request, 'This phone number already exists')
                        return redirect('/users/register')
                else:
                    customer = False

                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exists')
                    return redirect('/users/register')

                if User.objects.filter(username=username).exists():
                    messages.error(request, 'This username already exists')
                    return redirect('/users/register')

                if password != confirm_password:
                    messages.error(request, 'Confirm password dose not match')
                    return redirect('/users/register')

                user = User()
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.password = make_password(password)
                user.is_active = True
                user.is_staff = True
                user.is_vendor = vendor
                user.is_customer = customer
                user.save()

                if user and user_type == 'vendor':
                    Vendor.objects.create(
                        phone=phone,
                        user=user,
                    )

                else:
                    Customer.objects.create(
                        phone=phone,
                        user=user,
                    )

                messages.success(request, 'User register successfully. Please Login')
                return redirect('/users/login')

            messages.error(request, 'Something went wrong * Field are required')
            return render(request, 'users/register.html')

        except ObjectDoesNotExist:
            messages.error(request, 'Something went wrong')
            return redirect('/users/register')

    return render(request, 'users/register.html')


def user_logout(request):
    logout(request)
    return redirect('/')


@is_login
def dashboard(request):
    return render(request, 'users/dashboard.html')
