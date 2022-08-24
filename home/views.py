from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product


def home(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'home.html', data)
