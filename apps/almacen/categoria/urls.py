from django.contrib import admin
from django.conf.urls import url
from apps.almacen.categoria.views import CategoriaList,CategoriaCreate,CategoriaUpdate

urlpatterns = [
    url(r'^categoria/$',CategoriaList.as_view(),name='categoria_listar'),
    url(r'^categoria/create$',CategoriaCreate.as_view(),name='categoria_create'),
    url(r'^categoria/edit/(?P<pk>\d+)$',CategoriaUpdate.as_view(),name='categoria_edit'),
]
