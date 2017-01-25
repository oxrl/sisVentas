from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.almacen.categoria.models import Categoria
from apps.almacen.categoria.forms import CategoriaForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from pure_pagination.mixins import PaginationMixin
# Create your views here.
class CategoriaList(PaginationMixin,ListView):
    queryset = Categoria.objects.all().order_by('id')
    template_name = "almacen/categoria/index.html"
    paginate_by = 5
    object = Categoria

class CategoriaCreate(CreateView):
    model= Categoria
    form_class= CategoriaForm
    template_name='almacen/categoria/categoria_form.html'
    success_url= reverse_lazy('almacen_cat:categoria_listar')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            if len(request.POST['nombre']) <= 3:
                messages.success(request,'El nombre debe ser mayor a tres caracteres')
                return HttpResponseRedirect(reverse('almacen_cat:categoria_create'))
            else:
                form.save()
                messages.success(request,'Se ha creado correctamente')
                return HttpResponseRedirect(self.get_success_url())
        else:
            messages.success(request,'Ha ocurrido un error al registrar tu categoria ')
            return HttpResponseRedirect(reverse('almacen_cat:categoria_create'))


class CategoriaUpdate(UpdateView):
    model=Categoria
    form_class=CategoriaForm
    template_name='almacen/categoria/categoria_form.html'
    success_url = reverse_lazy('almacen_cat:categoria_listar')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_categoria = kwargs['pk']
        categoria = self.model.objects.get(id=id_categoria)
        form = self.form_class(request.POST, instance=categoria)
        if len(request.POST['nombre']) <= 3:
                messages.success(request,'El nombre debe ser mayor a tres caracteres')
                error=True
        else:
            if form.is_valid():
                form.save()
                messages.success(request,'Se ha actualizado correctamente')
                return HttpResponseRedirect(self.get_success_url())
            else:
                return HttpResponseRedirect(reverse('almacen_cat:categoria_edit', kwargs={'pk':id_categoria}))

        return HttpResponseRedirect(reverse('almacen_cat:categoria_edit', kwargs={'pk':id_categoria}))

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'almacen/categoria/categoria_delete.html'
    success_url = reverse_lazy('almacen_cat:categoria_listar')
