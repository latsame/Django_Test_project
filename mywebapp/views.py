from django.shortcuts import render
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import  Home,About, Profile, Category, Skills, Techer,Techert,Blog

def index(request):

    # Home
    
    
    return render(request, 'index.html')
    # About
def about(request):
    about = About.objects.latest('updated')

    profiles = Profile.objects.filter(about=about)
    return render(request, 'about.html',{'about':about,'profiles':profiles})
    # Skills
def teacher(request):    
    # Portfolio
    portfolios = Techer.objects.all()
#techer2

    portfolior = Techert.objects.all()
    return render(request, 'teacher.html',{'portfolios':portfolios,'portfolior':portfolior})
#blog post
def blog(request):

    blogs = Blog.objects.all()
    categories = Category.objects.all()

    return render(request, 'blog.html',{'blogs':blogs,'categories':categories})

# def dashboard(request):
    
#     student = Student.objects.all().order_by('-pk')
    
#     return render(request, 'dashboard.html', {'student':student})