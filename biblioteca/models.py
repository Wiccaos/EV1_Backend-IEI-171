from django.db import models
import datetime

ahora = datetime.datetime.now

# Create your models here.


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=False)
    nacionalidad = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nacionalidad


class Autor(models.Model):
    id_nacionalidad = models.ForeignKey(
        Nacionalidad, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=250, null=False)
    pseudonimo = models.CharField(max_length=50, blank=True, default='')
    biografia = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.pseudonimo != '':
            return self.pseudonimo
        else:
            return self.nombre


class Comuna(models.Model):
    codigo_comuna = models.CharField(max_length=5, null=False)
    nombre_comuna = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_comuna


class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False)
    calle = models.CharField(max_length=50, null=False, default='')
    numero = models.CharField(max_length=10, null=False, default='')
    departamento = models.CharField(max_length=10, blank=True, default='')
    detalles = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comuna: {self.id_comuna}, Calle: {self.calle} N°: {self.numero}'


class Biblioteca(models.Model):
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, null=True)
    nombre_biblioteca = models.CharField(max_length=100, null=False)
    web = models.CharField(max_length=255, blank=True, default='')
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_biblioteca


class Lector(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, null=False)
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, null=True)
    rut_lector = models.IntegerField(null=False, unique=True)
    digito_verificador = models.CharField(max_length=1, null=False)
    nombre_lector = models.CharField(max_length=255, null=False)
    correo_lector = models.CharField(max_length=255, blank=True, default='')
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_lector


class TipoCategoria(models.Model):
    tipo_categoria = models.CharField(max_length=50, null=False)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo_categoria


class Categoria(models.Model):
    id_tipo_categoria = models.ForeignKey(
        TipoCategoria, on_delete=models.CASCADE, null=False)
    categoria = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=255, blank=True, default='')
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoria


class Libro(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, null=False)
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)
    titulo = models.CharField(max_length=255, null=False)
    paginas = models.IntegerField(null=False)
    copias = models.IntegerField(null=False)
    ubicacion = models.CharField(max_length=255, null=False)
    fisico = models.BooleanField(default=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.titulo}, De: {self.id_autor}'


class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=False)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE, null=False)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True)
    fecha_retorno = models.DateTimeField(null=True)