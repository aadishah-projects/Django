from django.db import models

# Create your models here.
#Understanding models
# passing Model class from model
class Student(models.Model):
    # id = models.AutoField()
    name =  models.CharField(max_length = 100)
    age = models.IntegerField(default= 18)
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField()
    # certificate = models.FileField()


class Car(models.Model):
    car_name = models.CharField(max_length= 500)
    speed = models.IntegerField(default = 89)
# just to identify which object represent which car    
    def __str__(self):
        return self.car_name 