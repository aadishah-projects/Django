from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Template Engine Transfering list to the index.html by django
def home(request):

    people = [
    {'name': 'Aditya Shah', 'age': 19},
    {'name': 'Sara Ali', 'age': 24},
    {'name': 'John Doe', 'age': 30},
    {'name': 'Emily Zhang', 'age': 27},
    {'name': 'Michael Brown', 'age': 35},
    {'name': 'Linda Kim', 'age': 22},
    {'name': 'Carlos Rivera', 'age': 28},
]

    return render(request, "home/index.html", context = {'peoples' : people} )

def success_page(request):
    return HttpResponse ("This is a success page")