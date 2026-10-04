from django import forms

class StudentForm(forms.Form):
    firstname = forms.CharField(label="First Name", max_length=100)
    lastname = forms.CharField(label="Last Name", max_length=100)
    course = forms.CharField(label="Course", max_length=100)
    age = forms.IntegerField(label="Age", min_value=0, max_value=100)       
 
