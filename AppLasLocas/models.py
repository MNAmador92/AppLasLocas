from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Servicio (models.Model): #p/CRUD

    def __str__(self):
        return f"{self.nombre} "

    nombre = models.CharField(max_length=150)
    info = models.TextField(null = True, blank = True)
    horarios = models.TextField(null = True, blank = True)
    costo = models.TextField(null = True, blank = True)

class SolicitudTurno (models.Model): #asociado a form FormularioTurno

    def __str__(self):
        return f"Pedido de turno de: {self.nombre} "

    servicio = models.CharField(max_length=200)
    mensaje = models.TextField(null = True, blank = True)
    nombre = models.CharField(max_length=150)
    tel = models.IntegerField()
    email = models.EmailField()

class Contacto (models.Model): #asociado a form FormularioContacto

    def __str__(self):
        return f"Mensaje de: {self.nombre} "

    mensaje = models.TextField(null = True, blank = True)
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    tel = models.IntegerField()

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to ="avatares", null = True, blank = True)

    def first(self, request):

        return self.filter(user=request.user.id)
