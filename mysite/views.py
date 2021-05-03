# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'rd', 'place':'mars'}
    return HttpResponse('hey!')

def about(request):
    return HttpResponse('hey!')