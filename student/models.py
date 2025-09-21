from django.db import models
from django.contrib.auth.models import User
from teacher.models import Courses

# Create your models here.

class Student(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    stu_name = models.CharField(max_length=80)
    stu_age = models.IntegerField()
    stu_conf = models.ManyToManyField("teacher.Courses", related_name="students")

    def __str__(self):
        return self.stu_name