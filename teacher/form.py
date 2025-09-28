from django import forms

from .models import Teacher, Courses



class CourseForm(forms.ModelForm):


    class Meta:
        model = Courses
        fields = "__all__" 
        
