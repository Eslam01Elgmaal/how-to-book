from django.db import models
from teacher.models import Courses

# Create your models here.

class Student(models.Model):
    stu_name = models.CharField(max_length=80)
    stu_age = models.IntegerField()
    stu_conf = models.ManyToManyField("teacher.Courses")

    def __str__(self):
        return self.stu_name