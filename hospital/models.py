from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="")
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField( max_length=10)
    phone = models.CharField(max_length=15, default="")
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    patient=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    date= models.DateField()
    time= models.TimeField()
    def __str__(self):
        return f"{self.patient}-{self.doctor}"

class Prescription(models.Model):
    patient=models.CharField(max_length=100)
    age=models.IntegerField()
    doctor=models.CharField(max_length=100)
    medicines=models.TextField()

class Bill (models.Model):
    medicines=models.TextField(max_length=100)
    amount= models.DecimalField(max_digits=10,decimal_places=2)