from django.contrib import admin
from .models import Nacionalidad, Autor, Comuna, Direccion

# Register your models here.
admin.site.register(Nacionalidad)
admin.site.register(Autor)
admin.site.register(Comuna)
admin.site.register(Direccion)