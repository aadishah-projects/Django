from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse ("<h1>Hello World, My name is Aditya Shah</h1>")

def success_page(request):
    return HttpResponse ("This is a success page")