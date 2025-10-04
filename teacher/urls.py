
from django.urls import path

from . import views

app_name= 'teacher'

urlpatterns = [
    path('', views.courses , name= "courses"),
    path('create', views.course_new , name= "new_course"),
    path('<int:id>', views.course , name= 'course'),
    path('edit/<int:id>', views.course_edit , name= 'edit_course'),
    path('delete/<int:id>', views.course_del , name= 'delete_course'),
]

