from django.urls import path
from . import views

urlpatterns = [
    # Path del Contacto
    path('', views.contact, name="contact"),
]