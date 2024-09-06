from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User , on_delete= models.PROTECT)
    category = models.CharField(max_length=100)

class Patient(models.Model):
    user = models.OneToOneField(User , on_delete= models.PROTECT)


class Service(models.Model) :
    date = models.DateField()
    type = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    price = models.IntegerField()
    status = models.CharField(max_length=50)


class Trans(models.Model):
    service = models.OneToOneField(Service)
    date = models.DateField()
