from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

class Image(models.Model):
    Imagename=models.CharField(max_length=30)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)

class Imagego(models.Model):
    Imagename=models.CharField(max_length=30)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Model=models.CharField(max_length=30)
    price=models.IntegerField()

class Registergo(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
    Imagename=models.CharField(max_length=30)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)