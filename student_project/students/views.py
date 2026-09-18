from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
def students(request):
    return render(request, 'student_home.html')
def about(request):
    return render(request, 'about.html')
def student_home(request):
    return render(request, 'student_home.html')
def contact(request):
    return render(request, 'contact.html')

def students(request):
    student_list = Student.objects.all()

    return render(
        request, 
        'student_home.html',
        {'students': student_list}
        )

# Create your views here.
