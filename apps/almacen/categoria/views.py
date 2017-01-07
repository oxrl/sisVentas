from django.shortcuts import render
from apps.almacen.categoria.models import Categoria
from django.views.generic import ListView
# Create your views here.
class CategoriaList(ListView):
    model = Categoria
    template_name = "almacen/categoria/index.html"
