from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    name  =  models.CharField(max_length=150)
    address  = models.CharField(max_length=200)
    bod=models.CharField(max_length=50)
    email=models.EmailField()
    train_name= models.CharField(max_length=100)
    journeyto = models.CharField(max_length=100)
    journeyfrom = models.CharField(max_length=100)

