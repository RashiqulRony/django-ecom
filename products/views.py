from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    data = {
        'products' : products
    }
    return render(request, 'products.html', data)


def new(request):
    return HttpResponse('New Products')
