from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, '')

def contact(request):
    return render(request, '')

def tracker(request):
    return render(request, '')

def search(request):
    return render(request, '')

def productview(request):
    return render(request, '')

def checkout(request):
    return render(request, '')
