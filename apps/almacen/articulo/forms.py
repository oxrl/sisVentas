from django import forms
from apps.almacen.categoria.models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'idarticulo',
            'nombre',
            'codigo',
            'categoria',
            'stock',
            'imagen',
            'estado',
        ]
        labels = {
            'idarticulo':'Nombre',
            'nombre':'Descripción',
            'codigo':'Codigo',
            'categoria':'Categoria',
            'stock':'Stock',
            'imagen':'Imagen',
            'estado':'Estado',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite la Categoría'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Digite la Descripción'}),
        }
