from users.forms import UserRegisterForm, UserEditForm
from users.models import Imagen

from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin


def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render(request, "AppGoldenCafe/padre.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"AppGoldenCafe/padre.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})


@login_required
def editar_perfil(request):
    usuario = request.user     # Obtiene la instancia del usuario actualmente autenticado a partir de la solicitud (request)
    if request.method == 'POST':  
            
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario) 
        # Crea una instancia del formulario UserEditForm, llenándolo con los datos enviados en la solicitud (request.POST y request.FILES) 
        # y utilizando la instancia del usuario actual como base para la edición
        if miFormulario.is_valid(): 
            
            if miFormulario.cleaned_data.get('imagen'): # Si se ha proporcionado una nueva imagen en el formulario
                if Imagen.objects.filter(user = usuario).exists(): # Si el usuario ya tiene una imagen asociada (existe un objeto Imagen para este usuario)
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen') # Actualiza la imagen existente con la nueva
                    usuario.imagen.save()  
                else:
                    avatar = Imagen(user = usuario, imagen = miFormulario.cleaned_data.get('imagen')) # Si no tiene img asociada, crea un nuevo objeto Imagen y lo asocia al usuario actual
                    avatar.save()
            
            miFormulario.save() # Guarda los cambios en los datos del usuario (incluyendo cualquier otro campo editado en el formulario)
            return render(request, "AppGoldenCafe/padre.html")
            

            """
            #Otra alternativa
            miFormulario.save()
        
            imagen = miFormulario.cleaned_data.get('imagen')
            if imagen:
                # Si se sube una nueva imagen, la asociamos al usuario
                instance, created = Imagen.objects.get_or_create(user=usuario)
                instance.imagen = imagen
                instance.save()
            return render(request, "AppGoldenCafe/padre.html", {'usuario': usuario})
            """
    else:  # Si es un GET (carga inicial de la página)
        miFormulario = UserEditForm(instance=usuario) # Crea una instancia del formulario UserEditForm, prellenándolo con los datos del usuario actual
        return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})
        # Renderiza la plantilla "users/editar_usuario.html", pasando el formulario y la instancia del usuario como contexto


class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")

