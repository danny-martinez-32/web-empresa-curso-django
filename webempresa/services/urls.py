from django.urls import path
from . import views

urlpatterns = [
    # Path del services
    path('', views.services, name="services"),
]