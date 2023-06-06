from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name','email','phone_number','studentID','address','show_image_pic',]
    search_fields = []
    list_filter = []

admin.site.register(Student, StudentAdmin)