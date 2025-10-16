from django.shortcuts import render
from rest_framework import viewsets
from .serializer import NacionalidadSerializer, AutorSerializer, ComunaSerializer, DireccionSerializer, BibliotecaSerializer, LibroSerializer, TipoCategoriaSerializer, CategoriaSerializer, LectorSerializer, PrestamoSerializer
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, TipoCategoria, Categoria, Libro, Prestamo
from rest_framework.authentication import SessionAuthentication 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect 


class MiVistaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
# Otras configuraciones de la vista... 


# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(request, "No ha sido posible Registrarlo. Por favor revise el formulario por errores.")
    else:
        form = UserCreationForm()
        return render(request, 'registro.html', {'form':form}) 

def vista_protegida(request):
    if not request.user.is_authenticated:
    # Redirecciona a login si el usuario no está autenticado
        return redirect('login')
    return render(request, 'vista_protegida.html')

def logout_view(request):
    # Cierra la sesión del usuario y limpia la data de SESSION
    logout(request)
    # Redirige a la página de inicio de sesión
    return redirect('login') 

@login_required 
def pag_inicio(request):
    # Almacenar data en SESSION
    request.session['mensaje_bienvenida'] = '¡Bienvenido!'

    # Obtener data desde SESSION
    mensaje_bienvenida = request.session.get('mensaje_bienvenida')
    return render(request, 'biblioteca/inicio.html')

    # Remover data desde SESSION
    if 'mensaje_bienvenida' in request.session:
        del request.session['mensaje_bienvenida']
    return render(request, 'biblioteca/inicio.html', {'message': mensaje_bienvenida}) 


class NacionalidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
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

