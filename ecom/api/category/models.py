from operator import truediv
from pyexpat import model
from turtle import update
from unicodedata import name
from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=30)
    discription = models.CharField(max_length=250)


    def __str__(self):
        return self.name