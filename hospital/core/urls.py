from django.urls import path
from .views import Login , Refresh , ServiceEdit , ServiceView , TransView

urlpatterns = [
    path('login/', Login.as_view()),
    path('refresh/', Refresh.as_view()),
    path('service/', ServiceView.as_view()),
    path('edservice/<int:pk>', ServiceEdit.as_view()),
    path('trans/' ,TransView.as_view()),
]