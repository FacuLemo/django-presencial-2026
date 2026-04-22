from django.shortcuts import render
from miniblog.models import Posteo

def saludar(request):
    posts = Posteo.objects.all()
    contexto = {"usuarios": ["Facu", "Juancito", "Pepito"], "posts":posts}
    return render(request, "holamundo/index.html", contexto)


def despedir(request):
    return render(request, "holamundo/despedir.html")
