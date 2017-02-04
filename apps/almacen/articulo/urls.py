from django.contrib import admin
from django.conf.urls import url
from apps.almacen.articulo.views import ArticuloList,ArticuloCreate,ArticuloDelete

urlpatterns = [
    url(r'^/$',ArticuloList.as_view(),name='articulo_listar'),
    url(r'^/create$',ArticuloCreate.as_view(),name='articulo_create'),
    url(r'^/delete/(?P<pk>\d+)$',ArticuloDelete.as_view(),name='articulo_delete'),
]
