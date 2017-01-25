from django.contrib import admin
from django.conf.urls import url
from apps.almacen.articulo.views import ArticuloList

urlpatterns = [
    url(r'^/$',ArticuloList.as_view(),name='articulo_listar'),

]
