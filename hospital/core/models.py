from django.db import models
from django.contrib.auth.models import User

class doctor(models.Model):
    user = models.OneToOneField(User , on_delete= models.PROTECT)
    category = models.CharField(max_length=100)

class patient(models.Model):
    user = models.OneToOneField(User , on_delete= models.PROTECT)


class service(models.Model) :
    date = models.DateField()
    type = models.CharField(max_length=100)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    price = models.IntegerField()
    status = models.CharField(max_length=50)


class Trans(models.Model):
    service = models.OneToOneField(service)
    date = models.DateField()

