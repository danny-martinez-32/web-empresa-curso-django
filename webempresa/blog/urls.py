from django.urls import path
from . import views

urlpatterns = [
    # Path del blog
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category") # Los parametros siempre son cadenas de caracteres con 'int' lo cambiamos a entero
]