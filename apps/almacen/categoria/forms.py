from django import forms
from apps.almacen.categoria.models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre',
            'descripcion',
        ]
        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Digite la Categoría'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Digite la Descripción'}),
        }
