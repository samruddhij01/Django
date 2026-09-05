from django.db import models

# Create your models here.
class student(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    contact=models.CharField(max_length=50)
    city=models.CharField(max_length=10)

class emp(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class faculty(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    
class player(models.Model):
    fullname=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
class artist(models.Model):
    fullname=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
class deveploper(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    
class register(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    password=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=200,default="pune")