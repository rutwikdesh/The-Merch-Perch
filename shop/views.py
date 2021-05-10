from django.db.models.base import ModelStateFieldsCacheDescriptor
from shop.models import Product, Contact
from django.shortcuts import render
from django.http import HttpResponse
import math


def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + math.ceil(n/4 - n//4)
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    
    # saving contact info to the database
    

    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, '')


def productview(request, id):
    product = Product.objects.filter(id=id)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    return render(request, '')
