from django.urls import path

from . import views

urlpatterns = [
    path("", views.saludar, name="saludo"),
    path("despedir/", views.despedir, name="adios"),
]
