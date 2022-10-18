from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class FormularioTurno (forms.Form):

    Servicio = forms.IntegerField()
    Comentario = forms.CharField()
    Nombre = forms.CharField()
    Teléfono = forms.IntegerField()
    Email = forms.EmailField()

class FormularioContacto (forms.Form):

    Comentario = forms.CharField()
    Nombre = forms.CharField()
    Email = forms.EmailField()
    Teléfono = forms.IntegerField()

class FormularioRegistro(UserCreationForm): 

    Nombre = forms.CharField()
    Teléfono = forms.IntegerField()
    Fecha_de_Nacimiento = forms.DateField()
    Email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    class Meta: 

        model = User 
        fields = ["username", "Nombre", "Fecha_de_Nacimiento", "Teléfono", "Email", "password1", "password2"]

class FormularioEditarUsuario(UserCreationForm): 

    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    Teléfono = forms.IntegerField(label="Ingrese su nuevo teléfono")
    Fecha_de_Nacimiento = forms.DateField()

    class Meta:

        model = User 
        fields = ["email", "password1", "password2", "Teléfono", "Fecha_de_Nacimiento"] 

class CambiarAvatar (forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["user", "imagen"]

