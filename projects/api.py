from .models import Project
from rest_framework import viewsets,permissions 
from .serializers import ProjectSerializer


class ProjectViewSet( viewsets.ModelViewSet ):
    #esto es todo el conjunto de datos del modelo
    queryset = Project.objects.all()
    #esto es el permiso que permite acceder a los datos en este caso cualquiera
    permission_classes =[permissions.AllowAny]
    serializer_class = ProjectSerializer 