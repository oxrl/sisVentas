from django.shortcuts import render
from apps.almacen.categoria.models import Categoria
from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
# Create your views here.
class CategoriaList(PaginationMixin,ListView):
    model = Categoria
    template_name = "almacen/categoria/index.html"
    paginate_by = 5
    object = Categoria
