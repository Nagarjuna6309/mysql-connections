from django.db import models

# Create your models here.


class school(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
    
class student(models.Model):
    name=models.CharField(max_length=100)
    cls=models.IntegerField()
    age=models.IntegerField()