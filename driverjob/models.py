from codecs import getencoder
from inspect import modulesbyfile
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DriverUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null= True)
    image = models.FileField(null=True)
    gender =models.CharField(max_length=10, null=True)
    type =models.CharField(max_length=15, null=True)
    def _str_ (self):
        return self.user.username

class Employer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null= True)
    image = models.FileField(null=True)
    gender =models.CharField(max_length=10, null=True)
    company =models.CharField(max_length=100, null=True)
    type =models.CharField(max_length=15, null=True)
    status =models.CharField(max_length=20, null=True)
    def _str_ (self):
        return self.user.username

class Job(models.Model):
    employer=models.ForeignKey(Employer,on_delete=models.CASCADE)
    start_date =models.DateField()
    end_date =models.DateField()
    title = models.CharField(max_length=100)
    salary =models.FloatField(max_length=20)
    image = models.FileField(null=True)
    description =models.CharField(max_length=200)
    experience =models.CharField(max_length=100)
    location =models.CharField(max_length=100)
    creationdate =models.DateField()
    def _str_ (self):
        return self.title 

class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverUser,on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()
    def _str_ (self):
        return self.id                      