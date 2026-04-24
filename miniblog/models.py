from django.db import models

# Si posteo NO tuviera el def __str__, cuando se lista
#  (por ejemplo,) en el admin, se vería de la siguiente forma:

#Posteo Object (1)

#Con el __str__ se muestra como el return del método, es decir:

#Mi primer Posteo, 5 likes. 22/04/2026



class Posteo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.titulo}, {self.likes} likes. {self.fecha_creacion}"
