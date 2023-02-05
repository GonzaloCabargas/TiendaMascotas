from django.db import models

# Create your models here.

class user(models.Model):
    id_user = models.IntegerField(primary_key=True , verbose_name="id usuario")
    nombre_user = models.CharField(max_length=50, verbose_name="nombre usuario")
    apellido = models.TextField(verbose_name="apellido")
    correo = models.CharField(max_length=100, verbose_name="correo")
    contrasena = models.CharField(max_length=20, verbose_name="contrasena")
    imagen = models.ImageField(upload_to="productos", null='true')


    def __str__(self):
        return self.id_user


class Producto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="id producto")
    nombre = models.CharField(max_length=50, verbose_name="nombre producto")
    descripcion = models.TextField(verbose_name="descripcion")
    precio = models.IntegerField(verbose_name="precio")
    imagen = models.ImageField(upload_to=("media/"))

    def __str__(self):
        return f"{self.nombre} -> {self.precio}"


class venta(models.Model):
    id_vta = models.IntegerField( verbose_name="id de la venta")
    neto_vta = models.IntegerField( verbose_name="neto")
    impuesto_vta = models.IntegerField( verbose_name="impuesto")
    total_vta = models.IntegerField( verbose_name="total")

    def __str__(self):
        return self.id_vta

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return  self.nombre