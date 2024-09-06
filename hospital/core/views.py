from .serializer import PatientSerializer , TransSerializer , ServiceSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated 
from .permision import IsAdminUser
from .models import Doctor , Patient , Service , Trans

class 


