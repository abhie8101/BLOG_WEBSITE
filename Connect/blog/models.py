from django.db import models

# Create your models here.
class profile(models.Model):
    user = models.CharField(max_length = 32)
    bio    = models.TextField()
    image = models.ImageField()
    gender = models.CharField(max_length = 10)


class blog(models.Model):
    author = models.CharField(max_length = 32)
    blogdata = models.TextField()
    time = models.DateTimeField()
