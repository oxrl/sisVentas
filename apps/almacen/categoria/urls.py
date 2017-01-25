from django.contrib import admin
from django.conf.urls import url
from apps.almacen.categoria.views import CategoriaList,CategoriaCreate,CategoriaUpdate,CategoriaDelete

urlpatterns = [
    url(r'^/$',CategoriaList.as_view(),name='categoria_listar'),
    url(r'^/create$',CategoriaCreate.as_view(),name='categoria_create'),
    url(r'^/edit/(?P<pk>\d+)$',CategoriaUpdate.as_view(),name='categoria_edit'),
    url(r'^/delete/(?P<pk>\d+)$',CategoriaDelete.as_view(),name='categoria_delete'),
]
