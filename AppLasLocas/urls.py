import imp
from django.urls import path 
from AppLasLocas.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

path ("", inicio, name = "Inicio"),
path ("about/", about, name = "About"),


############  F O R M U L A R I O S ############

path ("turnosonline/", formularioTurnosOnline, name = "TurnosOnline"),
path ("contacto/", formularioContacto, name = "Contacto"),

############# C R U D . V I S T A S . T I P O . C L A S E S #################

path ("listaservicios/", ListaServicio.as_view(), name = "VerServicios"),
path ("listaservicios/<int:pk>", DetalleServicio.as_view(), name="DetalleServicio"),
path ("listaservicios/nuevo/", CrearServicio.as_view(), name = "CrearServicio"),
path ("listaservicios/editar/<int:pk>", ActualizarServicio.as_view(), name="ActualizarServicio"),
path ("listaservicios/borrar/<int:pk>", BorrarServicio.as_view(), name="BorrarServicio"),

# B U S C A R #

path("busquedaservicios/", busquedaServicio),
path("resultados/", resultado),

#################### L O G I N . Y . L O G O U T #####################

path ("login/", iniciar_sesion, name ="Login"),
path ("logout/", LogoutView.as_view(template_name="AppLasLocas/logout.html"), name = "Logout"),


######################### R E G I S T E R . & . E D I T . U S E R ##########################

path("registro/", registro, name = "Registrarse"),
path ("editarusuario/", editarUsuario, name = "EditarUsuario"), #asociada tmb a vista cambiarFotoPerfil
path ("subirimagen/", cambiarFotoPerfil, name = "Avatar"),

########################### B L O G S ###############################

path ("infounias/", blogUnias, name = "Unias"),
path ("infofaciales/", blogTratFraciales, name = "Faciales"),
path ("infopestanias/", blogPestanias, name = "Pestanias"),

]