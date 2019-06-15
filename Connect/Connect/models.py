from django.db import models
# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length = 20)
    PassWord = models.CharField(max_length = 20)
    Email = models.EmailField()
