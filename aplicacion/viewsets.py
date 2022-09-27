from rest_framework import viewsets
from . import models
from . import serializers

class EntidadViewset (viewsets.ModelViewSet):
    queryset=models.Usuario.objects.all()
    serializer_class=serializers.EntidadSerializer