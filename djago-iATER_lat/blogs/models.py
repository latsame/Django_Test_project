from django.db import models

# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    writer = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="blogImages",blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name