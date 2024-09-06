from rest_framework.serializers import ModelSerializer
from .models import Patient , Doctor , Service , Trans

class TransSerializer(ModelSerializer):
    class Meta:
        model = Trans
        fields = '__all__'

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'