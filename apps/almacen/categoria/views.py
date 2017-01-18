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
    model = Categoria
    template_name = "almacen/categoria/index.html"
    paginate_by = 5
    object = Categoria

class CategoriaCreate(CreateView):
    model= Categoria
    form_class= CategoriaForm
    template_name='almacen/categoria/categoria_form.html'
    success_url= reverse_lazy('almacen:categoria_listar')

    def post(self, request, *args, **kwargs):
        error=False
        self.object = self.get_object
        form = self.form_class(request.POST)
        if len(request.POST['nombre']) <= 3:
            messages.success(request,'El nombre debe ser mayor a tres caracteres')
            error=True
        if form.is_valid() and error != True:
            categoria = form.save(commit=False)
            categoria.save()
            messages.success(request,'Se ha creado correctamente')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(reverse('almacen:categoria_create'))

class CategoriaUpdate(UpdateView):
    model=Categoria
    form_class=CategoriaForm
    template_name='almacen/categoria/categoria_form.html'
    success_url = reverse_lazy('almacen:categoria_listar')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_categoria = kwargs['pk']
        categoria = self.model.objects.get(id=id_categoria)
        form = self.form_class(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request,'Se ha actualizado correctamente')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.success(request,'Error al ingresar los datos')
            return HttpResponseRedirect(reverse('almacen:categoria_edit', kwargs={'pk':id_categoria}))

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'almacen/categoria/categoria_delete.html'
    success_url = reverse_lazy('almacen:categoria_listar')
