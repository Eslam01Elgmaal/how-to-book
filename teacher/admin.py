from django.contrib import admin

from .models import Teacher, Courses

# Register your models here.


class TeacAdmin(admin.ModelAdmin):
    list_display = ('tea_name', 'discraptions')

class CoursAdmin(admin.ModelAdmin):
    list_display = ('cour_name', 'cour_date', 'cour_price')


admin.site.register(Teacher, TeacAdmin)
admin.site.register(Courses, CoursAdmin)
