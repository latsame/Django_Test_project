from django.shortcuts import render
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Student
# Create your views here.

def dashboard(request):
    
    student = Student.objects.all().order_by('-pk')
    
    return render(request, 'dashboard.html', {'student':student})