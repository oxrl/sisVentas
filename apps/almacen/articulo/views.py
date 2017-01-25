from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.almacen.articulo.models import Articulo
from django.views.generic import ListView
# Create your views here.
class ArticuloList(ListView):
    queryset = Articulo.objects.all().order_by('idarticulo')
    template_name = "almacen/articulo/index.html"
    paginate_by = 5
    object = Articulo
