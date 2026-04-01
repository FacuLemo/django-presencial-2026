from django.shortcuts import render


def saludar(request):
    contexto = {"usuarios": ["Facu", "Juancito", "Pepito"]}
    return render(request, "holamundo/index.html", contexto)


def despedir(request):
    return render(request, "holamundo/despedir.html")
