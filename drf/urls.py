"""
URL configuration for djangomio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from rest_framework import permissions
from biblioteca import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación API Biblioteca",
        default_version="v1",
        description="Biblioteca",
        terms_of_service="https://google.com/policies/terms/",
        contact=openapi.Contact(email="wiccaos.moon@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name='home'),

    # URLs aplicación
    path('biblioteca/', include('biblioteca.urls')),

    # URLs documentación
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # URL's de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]