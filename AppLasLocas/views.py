from django.shortcuts import render
from AppLasLocas.models import *
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

################## I N I C I O #####################

def inicio (request):

    return render (request, "AppLasLocas/inicio.html")

################# L O G I N .  R E G I S T R O . & . E D I T - U S E R ############################

def iniciar_sesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST) 

        if form.is_valid(): 

            usuario = form.cleaned_data.get("username") 
            contra = form.cleaned_data.get("password") 

            user = authenticate(username=usuario, password=contra)

            if user:

                login(request, user)

                return render (request, "AppLasLocas/inicio.html")
        
        else:

            return render (request, "AppLasLocas/inicio.html", {"mensaje": f"Datos inválidos!"})

    else:

        form = AuthenticationForm()

    return render (request, "AppLasLocas/login.html", {"formu3":form})

def registro (request):

    if request.method == "POST":

        formu = FormularioRegistro(request.POST)

        if formu.is_valid():

            nombreUsuario = formu.cleaned_data["username"]
            formu.save() 

            return render (request, "AppLasLocas/inicio.html", {"mensaje": f"Usuario {nombreUsuario} creado!"}) 

    else:
        
        formu = FormularioRegistro() 

    return render(request, "AppLasLocas/registro.html", {"formu4": formu})

@login_required
def editarUsuario (request):

    usuarioOnline = request.user 

    if request.method == "POST": 

        formuEditUser = FormularioEditarUsuario(request.POST) 

        if formuEditUser.is_valid(): 

            info = formuEditUser.cleaned_data 

            usuarioOnline.email = info ["email"] 
            usuarioOnline.password1 = info ["password1"] 
            usuarioOnline.password2= info ["password2"]
            usuarioOnline.Teléfono = info ["Teléfono"]
            usuarioOnline.Fecha_de_Nacimiento= info ["Fecha_de_Nacimiento"]

            usuarioOnline.save() 

            return render (request, "AppLasLocas/inicio.html") 

    else:

        formuEditUser = FormularioEditarUsuario(initial= {"email": usuarioOnline.email} ) 


    return render (request, "AppLasLocas/editarUsuario.html", {"formuEditar": formuEditUser, "usuario": usuarioOnline} )

################################# C A M B I A R . F O T O . D E . P E R F I L ##################################

@login_required
def cambiarFotoPerfil(request):

    if request.method == "POST":

        formuImagen = CambiarAvatar(request.POST, request.FILES)

        if formuImagen.is_valid():

            info = formuImagen.cleaned_data
            
            avatar = Avatar(user=request.user, imagen=info["imagen"])

            avatar.save()

            return render (request, "AppLasLocas/inicio.html")

    else:

        formImagen = CambiarAvatar()

    return render (request, "AppLasLocas/agregarImg.html", {"imagen": formImagen})


################## A B O U T . & . B L O G S ########################

def about (request):

    return render (request, "AppLasLocas/about.html")

def blogUnias (request):

    return render (request, "AppLasLocas/blogUnias.html")

def blogTratFraciales (request):

    return render (request, "AppLasLocas/blogFaciales.html")

def blogPestanias (request):

    return render (request, "AppLasLocas/blogPestanias.html")

########################  F O R M U L A R I O S #########################
@login_required
def formularioTurnosOnline (request):

    if request.method=="POST":

        formuTurno = FormularioTurno(request.POST)

        if formuTurno.is_valid():

            info = formuTurno.cleaned_data

            turno = SolicitudTurno(servicio = info ["Servicio"], mensaje = info["Comentario"], nombre = info["Nombre"], tel = info ["Teléfono"], email = info ["Email"]) 
            turno.save()

            return render (request, "AppLasLocas/inicio.html") 
            
    else:
        
        formuTurno = FormularioTurno()

    return render(request, "AppLasLocas/solicitarTurno.html", {"formuTurno":formuTurno}) 

def formularioContacto (request):

    if request.method=="POST":

        formuContacto = FormularioContacto(request.POST)

        if formuContacto.is_valid():

            info = formuContacto.cleaned_data

            datos = Contacto(mensaje = info ["Comentario"], nombre = info["Nombre"], email = info ["Email"], tel = info ["Teléfono"]) 
            datos.save()

            return render (request, "AppLasLocas/inicio.html") 
            
    else:
        
        formuContacto = FormularioContacto()

    return render(request, "AppLasLocas/contacto.html", {"formuContacto":formuContacto}) 

####################### C R U D ##########################

class ListaServicio (ListView): #Read

    model = Servicio
    template_name= "AppLasLocas/listaServicios.html"

class DetalleServicio (DetailView):

    model = Servicio

class CrearServicio (LoginRequiredMixin, CreateView): #Create

    model = Servicio
    success_url = "/AppLasLocas/listaServicios"
    fields = ["nombre", "info", "horarios", "costo"]

class ActualizarServicio (LoginRequiredMixin,UpdateView): #update

    model = Servicio
    success_url = "/AppLasLocas/listaServicios"
    fields = ["horarios","costo"]

class BorrarServicio (LoginRequiredMixin, DeleteView): #delete

    model = Servicio
    success_url = "/AppLasLocas/listaServicios"

# B U S C A R #

def busquedaServicio (request):

    return render (request, "AppCoder/listaServicios.html")

def resultado(request):

    if request.GET["nombre"]:

        busqueda = request.GET["nombre"]
        servicio = Servicio.objects.filter(nombre__icontains=busqueda) 

        return render (request, "AppLasLocas/resultados.html", {"servicio":servicio, "busqueda": busqueda})

    else:

        mensaje = "No enviaste datos."
        
        
    return render (request, "AppLasLocas/resultados.html", {"mensaje":mensaje})













