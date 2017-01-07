from django.contrib import admin
from django.conf.urls import url
from apps.almacen.categoria.views import CategoriaList

urlpatterns = [
    url(r'^categoria',CategoriaList.as_view(),name='categoria'),
]
