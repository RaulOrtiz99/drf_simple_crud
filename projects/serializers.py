from rest_framework import serializers 

from .models import Project 

#TODO la clase serializar crea un objeto de la clase project que puede ser consultado 
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        #campos que se van a consultar 
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        #con esta linea decimos que este dato solo se puede leer
        read_only_fields = ('created_at',)