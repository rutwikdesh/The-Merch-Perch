from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, '')

def contact(request):
    return render(request, '')