# using many data for learning
from faker import Faker
import random
from .models import *
fake   = Faker(['en_US'])

def seed_db(n = 90)->None:
    try:
        for i in range(0, n):

            department_obj = Department.objects.all()
            random_index = random.randint(0, len(department_obj)-1)
            department = department_obj[random_index]
            student_id = f"080BCT{random.randint(0,200)}"
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

# def seed_db_delete(n = 50)-> None:
#     for i in range(0, n):
#         st_obj = Student.objects.all()
#         st_obj.delete()
#         st_id_obj = StudentID.objects.all()
#         st_id_obj.delete()
