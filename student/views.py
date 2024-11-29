from django.shortcuts import render
from .models import *
# Create your views here.

def get_student(request):
    queryset = Student.objects.all()
    return render(request, 'student.html', {'queryset' : queryset})