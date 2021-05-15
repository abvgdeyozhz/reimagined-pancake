from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    return HttpResponse('Hello World')

def test(request):
    print(request)
    return HttpResponse('Hello from test')
