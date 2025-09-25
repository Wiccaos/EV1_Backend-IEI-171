from django.shortcuts import render
from rest_framework import viewsets
from .serializer import NacionalidadSerializer, AutorSerializer, ComunaSerializer, DireccionSerializer, BibliotecaSerializer, LibroSerializer, TipoCategoriaSerializer, CategoriaSerializer, LectorSerializer, PrestamoSerializer
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo

# Create your views here.

def pag_inicio(request):
    return render(request, 'biblioteca/inicio.html')


class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer


class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer


class TipoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer