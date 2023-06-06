from django.db import models
from ctypes import addressof
from distutils.command.upload import upload
from email.mime import image
from django.utils.html import format_html
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='student_image')
    phone_number = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    studentID = models.CharField(max_length=10)
    address = models.CharField(max_length=50, null=True)

    def show_image_pic(self):
        if self.image:
            return format_html('<img src="%s" height="50px">' % self.image.url)
        return 'NULL'
    show_image_pic.allow_tags = True




    def __str__(self):
        return self.user.username