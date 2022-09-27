from dataclasses import field
from rest_framework import serializers
from .models import Usuario

class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'