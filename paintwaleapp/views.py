from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the paintwale index.")

def home(request):
    return render(request, 'paintwaleapp/home.html')

def about(request):
    return render(request, 'paintwaleapp/about.html')