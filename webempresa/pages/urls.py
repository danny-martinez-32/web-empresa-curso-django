from django.urls import path
from . import views

urlpatterns = [
    # Path del blog
    path('<int:page_id>/<slug:page_slug>', views.page, name="page"), # Los parametros siempre son cadenas de caracteres con 'int' lo cambiamos a entero
]