from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from products.models import Product


def home(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'home.html', data)

