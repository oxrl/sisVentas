from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.almacen.articulo.models import Articulo
from apps.almacen.articulo.forms import ArticuloForm
from django.views.generic import ListView,CreateView,UpdateView
# Create your views here.
class ArticuloList(ListView):
    queryset = Articulo.objects.all().order_by('idarticulo')
    template_name = "almacen/articulo/index.html"
    paginate_by = 5
    success_url= reverse_lazy('almacen_art:articulo_listar')

class ArticuloDelete(UpdateView):
    model=Articulo
    success_url = reverse_lazy('almacen_art:articulo_listar')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_articulo = kwargs['pk']
        Articulo = self.model.objects.get(idarticulo=id_articulo)
        Articulo.estado='0'
        Articulo.save()
        return HttpResponseRedirect(reverse('almacen_art:articulo_listar'))

class ArticuloCreate(CreateView):
    model= Articulo
    form_class= ArticuloForm
    template_name='almacen/articulo/articulo_form.html'
    success_url= reverse_lazy('almacen_art:articulo_listar')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            if len(request.POST['nombre']) <= 3:
                messages.success(request,'El nombre debe ser mayor a tres caracteres')
                return HttpResponseRedirect(reverse('almacen_art:articulo_create'))
            else:
                form.save()
                messages.success(request,'Se ha creado correctamente')
                return HttpResponseRedirect(self.get_success_url())
        else:
            messages.success(request,'Ha ocurrido un error al registrar tu categoria ')
            return HttpResponseRedirect(reverse('almacen_art:articulo_create'))
