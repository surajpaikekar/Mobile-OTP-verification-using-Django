from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('validate-otp/', views.validate_otp, name='validate_otp'),
]
