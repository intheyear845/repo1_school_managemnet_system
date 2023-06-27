from django.urls import path
from . import views

urlpatterns=[
    path ('students_home/', views.getstudenthome, name="studenthome"),
    path ('student_registration/', views.addstudents, name="studentregistration")
]
