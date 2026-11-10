from django.db import models
from .categoria import Categoria    

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']