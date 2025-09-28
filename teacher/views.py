from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView      
from .models import Teacher, Courses

from .form import CourseForm


# Create your views here.


def courses(request):
    all_courses = Courses.objects.all()
    
    return render(request,"teacher/course_list.html",{"all_courses":all_courses})






def course(request, id):
    lesson = Courses.objects.get(id=id)

    return render(request,"teacher/course_detail.html",{"lesson":lesson})   




def course_edit(request, id):
    lesson = Courses.objects.get(id=id)
    if request.method == "POST":
        form = CourseForm(request.POST , instance=lesson)
        if form.is_valid():
            form.save()
            return redirect("home:courses") 

    else:
        form= CourseForm(instance=lesson)

    return render (request, "teacher/course_edit.html", {"form":form} )


def course_new(request):

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:courses") 

    else:
        form= CourseForm()

    return render (request, "teacher/course_new.html", {"form":form} )





"""

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
    
"""
