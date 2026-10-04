from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from . forms import StudentForm

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
def students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                firstname=form.cleaned_data["firstname"],
                lastname=form.cleaned_data["lastname"],
                course=form.cleaned_data["course"],
                age=form.cleaned_data["age"],
            )
    else:
        form = StudentForm()

    return render(request, "student_home.html", {"form": form})

# Create your views here.
