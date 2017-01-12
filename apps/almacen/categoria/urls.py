from django.contrib import admin
from django.conf.urls import url
from apps.almacen.categoria.views import CategoriaList,CategoriaCreate

urlpatterns = [
    url(r'^categoria/$',CategoriaList.as_view(),name='categoria_listar'),
    url(r'^categoria/create$',CategoriaCreate.as_view(),name='categoria_create'),
]
