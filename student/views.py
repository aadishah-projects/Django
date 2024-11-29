from django.shortcuts import render
from .models import *
# Create your views here.
from django.core.paginator import Paginator

def get_student(request):
    queryset = Student.objects.all()

    paginator = Paginator(queryset, 25)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    print(page_obj.object_list) # This is how data is stored.. 
    return render(request, 'student.html', {'queryset' : page_obj})

# Paginator from official documentation
# def listing(request):
#     contact_list = Contact.objects.all()
#     paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, "list.html", {"page_obj": page_obj})