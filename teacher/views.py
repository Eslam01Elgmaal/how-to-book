from django.shortcuts import render   
from django.views.generic import ListView, DetailView      
from .models import Teacher, Courses


# Create your views here.

class CoursesList(ListView):
    model = Courses
    context_object_name = 'courses'
    template_name=''
    def get_queryset(self):
        return Courses.objects.select_related('Teacher')
    





class CoursesDetail(DetailView):
    model = Courses
    template_name=''
    context_object_name = 'course'
    def get_queryset(self):
        return Courses.objects.select_related('Teacher').prefetch_related('students')
    
    