from django.db import models

class Usuario(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    ciudad=models.CharField(max_length=20)
    


# Create your models here.
