from django.db import models
from ctypes import addressof
from distutils.command.upload import upload
import email
from email.mime import image
from django.utils.html import format_html
from django.contrib.auth.models import User
# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



# SKILLS SECTION

class Category(models.Model):
    

    updated = models.ImageField(upload_to='pictures/')
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.ImageField(upload_to='picture/')



# PORTFOLIO SECTION

class Techer(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.CharField(max_length=200)

    def __str__(self):
        return f'Techer {self.id}'


class Techert(models.Model):
    image = models.ImageField(upload_to='pictures/')
    link = models.CharField(max_length=200)

    def __str__(self):
        return f'Techert {self.id}'

class Blog(models.Model):
    image = models.ImageField(upload_to='picture/')
    

    def __str__(self):
        return f'Blog {self.id}'


# class Student(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='student_image')
#     phone_number = models.CharField(max_length=50)
#     email= models.EmailField(max_length=50)
#     studentID = models.CharField(max_length=10)
#     address = models.CharField(max_length=50, null=True)

#     def show_image_pic(self):
#         if self.image:
#             return format_html('<img src="%s" height="50px">' % self.image.url)
#         return 'NULL'
#     show_image_pic.allow_tags = True




#     def __str__(self):
#         return self.user.username
