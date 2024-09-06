from .serializer import PatientSerializer , TransSerializer , ServiceSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permisions import IsSuperUser
from .models import Doctor , Patient , Service , Trans

class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

class ServiceView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend , filters.OrderingFilter ,filters.SearchFilter]
    ordering_fields = ["date" , "price"]
    search_fields = '__all__'
    filterset_fields = ["date"]
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        elif self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        return super(ServiceView, self).get_permissions()
    
    def get_queryset(self):
        if self.request.method == 'GET':
            return Service.objects.filter(patient__user = self.request.user)
    

class ServiceEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminUser]

    filter_backends = [DjangoFilterBackend , filters.OrderingFilter ,filters.SearchFilter]
    ordering_fields = ["date" , "price"]
    search_fields = '__all__'
    filterset_fields = ["date"]


class TransView(generics.ListCreateAPIView):
    queryset = Trans.objects.all()
    serializer_class = TransSerializer

    filter_backends = [DjangoFilterBackend , filters.OrderingFilter]
    ordering_fields = ["date"]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]

        elif self.request.method == 'GET':
            self.permission_classes = [IsSuperUser]
        return super(ServiceView, self).get_permissions()
    
    def get_queryset(self):
        return Trans.objects.filter(service__patient= self.request.user)