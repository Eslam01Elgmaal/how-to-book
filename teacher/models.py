from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Teacher(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    tea_name = models.CharField(max_length=90)
    discraptions = models.CharField( max_length=500)



    def __str__(self):

        return self.tea_name
    

class Courses(models.Model):


    cour_name = models.CharField(max_length=60)
    cour_date = models.DateField(default=datetime.date.today)
    cour_price = models.DecimalField(max_digits=10, decimal_places=2)
    teachar_conf = models.ForeignKey("Teacher",on_delete=models.CASCADE, related_name="courses")



    def __str__(self):
        return self.cour_name

    
