from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación") # Solo al crearse
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización") # Cada que se actualiza

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['order', 'title'] # "-" antes del campo orderna de manera descendente

    def __str__(self):
        return self.title