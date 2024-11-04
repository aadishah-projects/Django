from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Template Engine Transfering list to the index.html by django
def home(request):

    people = [
    {'name': 'Aditya Shah', 'age': 19},
    {'name': 'Sara Ali', 'age': 24},
    {'name': 'John Doe', 'age': 7},
    {'name': 'Emily Zhang', 'age': 27},
    {'name': 'Michael Brown', 'age': 35},
    {'name': 'Linda Kim', 'age': 6},
    {'name': 'Carlos Rivera', 'age': 28},
]
    text = """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam architecto earum, molestiae corporis maiores vel deleniti quaerat debitis reiciendis numquam?
    """
    return render(request, "home/index.html", context = {'peoples' : people ,'text' : text} )

def success_page(request):
    return HttpResponse ("This is a success page")