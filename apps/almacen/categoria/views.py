from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.almacen.categoria.models import Categoria
from apps.almacen.categoria.forms import CategoriaForm
from django.views.generic import ListView,CreateView,UpdateView
from pure_pagination.mixins import PaginationMixin
# Create your views here.
class CategoriaList(PaginationMixin,ListView):
    model = Categoria
    template_name = "almacen/categoria/index.html"
    paginate_by = 5
    object = Categoria

class CategoriaCreate(CreateView):
    model= Categoria
    form_class= CategoriaForm
    template_name='almacen/categoria/categoria_form.html'
    success_url= reverse_lazy('almacen:categoria_listar')

class CategoriaUpdate(UpdateView):
    model=Categoria
    form_class=CategoriaForm
    template_name='almacen/categoria/categoria_form.html'
    success_url = reverse_lazy('almacen:categoria_listar')
