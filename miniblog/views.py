from django.shortcuts import render, redirect
from .models import Posteo
from .forms import PosteoForm
# Create your views here.

def get_posts(request):
    posts = Posteo.objects.all()
    contexto = {"posts":posts}
    return render(request, "miniblog/index.html", contexto)

def crear_posteo(request):
    if request.method == 'POST':
        form = PosteoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adios')
        else:
            return redirect('crear')
    else: #get
        form = PosteoForm()
    
    return render(request, 'miniblog/crear.html', {"form":form})


