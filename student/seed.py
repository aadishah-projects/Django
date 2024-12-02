# using many data for learning
from faker import Faker
import random
from .models import *
fake   = Faker(['en_US'])
from django.db.models import Sum


def create_subjects_marks():
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject  = subject,
                    student = student,
                    marks = random.randint(0, 100)
                )

    except  Exception as e:
        print(e)


def seed_db(n = 1000)->None:
    try:
        for i in range(0, n):

            department_obj = Department.objects.all()
            random_index = random.randint(0, len(department_obj)-1)
            department = department_obj[random_index]

            # student_id = f"080BCT{random.randint(0,200)}"
            student_id = f"080PUL{i}"

            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 40)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id  = student_id)
            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )
    except Exception as e:
        print(e)

def seed_db_delete(n = 181)-> None:
    for i in range(0, n+ 1 ):
        st_obj = Student.objects.all()
        st_obj.delete()
        st_id_obj = StudentID.objects.all()
        st_id_obj.delete()


def generate_report_card():
    ranks = Student.objects.annotate(marks = Sum("studentmarks__marks")).order_by('-marks')
    
    i = 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
        i = i + 1
        