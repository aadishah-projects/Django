from django.shortcuts import render
from .models import *
# Create your views here.
from django.core.paginator import Paginator
from django.db.models import Q


def get_student(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search ) |
            Q(department__department__icontains = search ) |
            Q(student_id__student_id__icontains = search ) |
            Q(student_email__icontains = search )|
            Q(student_age__icontains = search )

              )
                                  
    search = request.GET.get('search', '')
    paginator = Paginator(queryset, 25)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    # print(page_obj.object_list) # This is how data is stored.. 

    page_list = []
    for num in range(1,page_obj.paginator.num_pages + 1):
        page_list.append(num)
    
    temp = (int(page_number) - 1) * 25 + 1
    count_list = []
    for num in range(temp, (int(page_number) * 25) + 1 ):
        count_list.append(num)

    zipped_list = zip(queryset,count_list)
    return render(request, 'student.html', {'queryset' : page_obj, 'page_list': page_list, 'search_query' : search, 'zipped_list' : zipped_list, 'page_number': int(page_number)} )

# Paginator from official documentation
# def listing(request):
#     contact_list = Contact.objects.all()
#     paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, "list.html", {"page_obj": page_obj})

def get_marks(request,student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    return render (request, 'marksheet.html', {'queryset' : queryset})