from django import forms
from apps.almacen.articulo.models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = [
            'idarticulo',
            'nombre',
            'codigo',
            'idcategoria',
            'stock',
            'imagen',
            'estado',
        ]
        labels = {
            'idarticulo':'Nombre',
            'nombre':'Descripción',
            'codigo':'Codigo',
            'idcategoria':'Categoria',
            'stock':'Stock',
            'imagen':'Imagen',
            'estado':'Estado',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite la Categoría'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Digite la Descripción'}),
        }
