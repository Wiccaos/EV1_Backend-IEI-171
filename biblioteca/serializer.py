from rest_framework import serializers
from .models import Comuna,Nacionalidad,Direccion,Autor

class Comuna_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Comuna
    fields = '__all__'

class Nacionalidad_Serializer(serializers.ModelSerializer):
 class Meta:
    model = Nacionalidad
    fields = '__all__'

class Direccion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class Autor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'