from django.db import models
from django.contrib.auth.models import User

class doctor(models.Model):
    user = models.OneToOneField(User , on_delete= models.PROTECT)
    category = models.charField(max_length=100)

class patient(models.Model):
    user = models.OneToOneField(User , on_delete= models.PROTECT)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)

class service(models.Model) :
    date = models.DateField()
    type = models.CharField(max_length=100)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    price = models.IntegerField()

# Create your models here.
