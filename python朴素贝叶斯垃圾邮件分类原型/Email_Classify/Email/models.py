from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Email(models.Model):
    sender = models.CharField(max_length=15)
    receiver = models.CharField(max_length=15)
    theme = models.CharField(max_length=15)
    message = models.CharField(max_length=2024)
    flag = models.CharField(max_length=15)
