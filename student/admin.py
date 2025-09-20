from django.contrib import admin

from .models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_dissplay = (
        'stu_name','stu_age',
    )


admin.site.register(Student, StudentAdmin)
