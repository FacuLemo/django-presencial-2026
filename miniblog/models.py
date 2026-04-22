from django.db import models

# Create your models here.


class Posteo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.titulo}, {self.likes} likes. {self.fecha_creacion}"
