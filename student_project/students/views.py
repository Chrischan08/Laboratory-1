from django.shortcuts import render
from django.http import HttpResponse
def students(request):
    return render(request, 'student_home.html')
def about(request):
    return render(request, 'about.html')
def student_home(request):
    return render(request, 'student_home.html')
# Create your views here.
