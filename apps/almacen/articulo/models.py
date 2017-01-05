from django.db import models
from apps.almacen.categoria.models import Categoria
# Create your models here.
class Articulo(models.Model):
    idarticulo = models.AutoField(primary_key=True)
    codigo= models.CharField(max_length=50)
    nombre= models.CharField(max_length=100)
    stock= models.IntegerField()
    descripcion=models.CharField(max_length=512)
    imagen=models.CharField(max_length=50)
    estado=models.CharField(max_length=20)
    idcategoria= models.ForeignKey(Categoria,db_column='idcategoria',null=True,blank=True,on_delete=models.CASCADE)
