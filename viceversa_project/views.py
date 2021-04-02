from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('')

def home(request):
    return render(request, 'home.html')

