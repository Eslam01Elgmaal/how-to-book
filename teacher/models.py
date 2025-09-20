from django.db import models
import datetime

# Create your models here.


class Teacher(models.Model):

    tea_name = models.CharField(max_length=90)
    discraptions = models.CharField( max_length=500)



    def __str__(self):

        return self.tea_name
    

class Courses(models.Model):


    cour_name = models.CharField(max_length=60)
    cour_date = models.DateField(auto_now=False, auto_now_add=False)
    cour_price = models.DecimalField(max_digits=5, decimal_places=2)
    teachar_conf = models.ForeignKey("Teacher",on_delete=models.CASCADE)



    def __str__(self):
        return self.cour_name

    
