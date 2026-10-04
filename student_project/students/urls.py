from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('about/', views.about, name='about'),
    path('student_home/', views.student_home, name='student_home'),
    path('contact/', views.contact, name='contact'),
]