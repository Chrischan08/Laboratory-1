from django.contrib import admin 
from .models import Student 

@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'firstname', 'lastname', 'course', 'age' ) 
    search_fields = ( 'firstname', 'lastname', 'course' ) 
    list_filter = ( 'course', 'age' ) 
    ordering = ('lastname', 'firstname') 
    list_per_page = 10 

admin.site.site_header = "Student Information System" 
admin.site.site_title = "Student Admin Portal" 
admin.site.index_title = "Student Records Management"
# Register your models here.
