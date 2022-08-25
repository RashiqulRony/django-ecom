from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def index(request):
    products = Product.objects.all()

    p = Paginator(products, 12)
    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)

    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)


    data = {
        'products': page_obj
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
