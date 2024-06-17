
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),

    path('add/', addStudent, name='addstudent'),
    path('update/<str:pk>/', updateStudent, name='update'),
    path('delete/<str:pk>/', deleteStudents.as_view(), name='delete')


]
