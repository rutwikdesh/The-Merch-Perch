from django.db.models.base import ModelStateFieldsCacheDescriptor
from shop.models import Product
from django.shortcuts import render
from django.http import HttpResponse
import math

def index(request):
    # products = Product.objects.all()
    # 
    # print(products)  
    # 
    # # params = {'no_of_slides':nSlides, 'range':range(1, nSlides), 'product':products}
    # allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    # 

    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + math.ceil(n/4 - n//4)
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, '')

def productview(request):
    return render(request, '')

def checkout(request):
    return render(request, '')
