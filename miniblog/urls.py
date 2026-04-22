from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_posts, name="posteos"),
    path("crear/", views.crear_posteo, name="crear"),

]
