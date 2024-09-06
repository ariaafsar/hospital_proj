from django.contrib.admin import register, ModelAdmin
from .models import Doctor , Patient , Service , Trans


@register(Doctor)
class DoctorAdmin(ModelAdmin):
    list_display = [
        'user',
        'category'
    ]


@register(Patient)
class PatientAdmin(ModelAdmin):
    list_display = [
        'user',
    ] 



@register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = [
        'date',
        'type',
        'doctor',
        'patient',
        'price',
        'status',
    ] 

@register(Trans)
class TransAdmin(ModelAdmin):
    list_display = [
        'service',
        'date'
    ] 
