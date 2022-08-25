from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    data = {
        'products' : products
    }
    return render(request, 'products.html', data)


def details(request, id):
    product = Product.objects.get(id=id)
    recent_products = Product.objects.all().exclude(id=id)
    data = {
        'product': product,
        'recent_products': recent_products,
    }

    return render(request, 'product-details.html', data)
