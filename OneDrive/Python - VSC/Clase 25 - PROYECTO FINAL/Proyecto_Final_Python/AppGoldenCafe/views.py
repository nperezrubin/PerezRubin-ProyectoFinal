from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from AppGoldenCafe.models import Cliente, Pedido, Sucursal
from AppGoldenCafe.forms import clienteFormulario, pedidoFormulario, sucursalFormulario



def inicio(req):
    return redirect('homepage')

def homepage(req):
    return render(req, "appgoldencafe/padre.html")

@login_required
def cliente(request):
    clientes = Cliente.objects.all()
    miFormulario = clienteFormulario()
    if request.method == "POST":
        
        if 'agregar_cliente' in request.POST:
            miFormulario = clienteFormulario(request.POST)  # creamos un objeto formulario con los datos enviados
            if miFormulario.is_valid():
                cliente = Cliente(nombre=miFormulario.cleaned_data['nombre'], email=miFormulario.cleaned_data['email']) #creo el objeto Cliente ya limpio
                cliente.save()                              # Guardamos el cliente en la BBDD
                return redirect('clientes')                 # redirigimos a clientes
            else:
                return render(request, "AppGoldenCafe/cliente.html", {'form': miFormulario})
            
        elif 'buscar_cliente' in request.POST:
            miFormulario = clienteFormulario()
            nombre = request.POST.get('nombre')
            if nombre:                       # respuesta = f"Estoy buscando el cliente con nombre: {req.GET['nombre']}
                clientes = Cliente.objects.filter(nombre__iexact=nombre)
                if clientes:
                    return render(request,"AppGoldenCafe/cliente.html", {'clientes': clientes, 'nombre': nombre})
                else:
                    mensaje = "El cliente ingresado no existe."
                    return render(request, "AppGoldenCafe/cliente.html", {'mensaje': mensaje, 'form': miFormulario})
            else:
                mensaje = "Por favor, ingresa un nombre para buscar."
                return render(request, "AppGoldenCafe/cliente.html", {'mensaje': mensaje, 'form': miFormulario})
        
        elif 'eliminar_cliente' in request.POST:
            miFormulario = clienteFormulario(request.POST)
            nombre = request.POST.get('nombre')
            if nombre:
                cliente = Cliente.objects.filter(nombre__iexact=nombre)
                if cliente:
                   cliente.delete()
                   return redirect('clientes')
                else:
                    mensaje = "El cliente ingresado no existe."
                    return render(request, "AppGoldenCafe/cliente.html", {'mensaje': mensaje, 'form': miFormulario})   
            else:
                mensaje = "Por favor, ingresa un nombre para eliminar"
                return render(request, "AppGoldenCafe/cliente.html", {'mensaje': mensaje, 'form': miFormulario})
        
        else:
            miFormulario = clienteFormulario()
            return render(request, "AppGoldenCafe/cliente.html", {'form': miFormulario})
               
    else:                                                   # si es un GET...
        miFormulario = clienteFormulario()                  # creamos un formulario vacio para mostrarlo inicialmente
        return render(request, "AppGoldenCafe/cliente.html", {'clientes': clientes, 'form': miFormulario})

@login_required
def editar_cliente(request, nombre):
    cliente = Cliente.objects.get(nombre=nombre)
    if request.method == 'POST':
        form = clienteFormulario(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = clienteFormulario(instance=cliente)
        return render(request, 'AppGoldenCafe/editar_cliente.html', {'form': form})

@login_required
def pedido(request):
    pedidos = Pedido.objects.all()
    miFormulario = pedidoFormulario()
    if request.method == "POST":
        
        if 'agregar_pedido' in request.POST:
            miFormulario = pedidoFormulario(request.POST)  
            if miFormulario.is_valid():
                pedido = Pedido(tipo_cafe=miFormulario.cleaned_data['tipo_cafe'], unidades=miFormulario.cleaned_data['unidades']) 
                pedido.save()                             
                return redirect('pedidos')                 
            else:
                return render(request, "AppGoldenCafe/pedido.html", {'form': miFormulario})
            
        elif 'buscar_pedido' in request.POST:
            miFormulario = pedidoFormulario()
            tipo_cafe = request.POST.get('tipo_cafe')
            if tipo_cafe:                       
                pedidos = Pedido.objects.filter(tipo_cafe__iexact=tipo_cafe)
                if pedidos:
                    return render(request,"AppGoldenCafe/pedido.html", {'pedidos': pedidos, 'tipo_cafe': tipo_cafe})
                else:
                    mensaje = "El pedido ingresado no existe."
                    return render(request, "AppGoldenCafe/pedido.html", {'mensaje': mensaje, 'form': miFormulario})
            else:
                mensaje = "Por favor, ingresa un pedido para buscar."
                return render(request, "AppGoldenCafe/pedido.html", {'mensaje': mensaje, 'form': miFormulario})
            
        elif 'eliminar_pedido' in request.POST:
            miFormulario = pedidoFormulario(request.POST)
            tipo_cafe = request.POST.get('tipo_cafe')
            if tipo_cafe:
                pedido = Pedido.objects.filter(tipo_cafe__iexact=tipo_cafe)
                if pedido:
                   pedido.delete()
                   return redirect('pedidos')
                else:
                    mensaje = "El pedido ingresado no existe."
                    return render(request, "AppGoldenCafe/pedido.html", {'mensaje': mensaje, 'form': miFormulario})   
            else:
                mensaje = "Por favor, ingresa un pedido para eliminar"
                return render(request, "AppGoldenCafe/pedido.html", {'mensaje': mensaje, 'form': miFormulario})

        else:
            miFormulario = pedidoFormulario()
            return render(request, "AppGoldenCafe/pedido.html", {'form': miFormulario})
               
    else:                                                   
        miFormulario = pedidoFormulario()                  
        return render(request, "AppGoldenCafe/pedido.html", {'pedidos': pedidos, 'form': miFormulario})

@login_required
def editar_pedido(request, tipo_cafe):
    pedido = Pedido.objects.get(tipo_cafe=tipo_cafe)
    if request.method == 'POST':
        form = pedidoFormulario(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedidos')
    else:
        form = pedidoFormulario(instance=pedido)
        return render(request, 'AppGoldenCafe/editar_pedido.html', {'form': form})

@login_required
def sucursal(request):
    sucursales = Sucursal.objects.all()
    miFormulario = sucursalFormulario()
    if request.method == "POST":
        
        if 'agregar_sucursal' in request.POST:
            miFormulario = sucursalFormulario(request.POST)  
            if miFormulario.is_valid():
                sucursal = Sucursal(barrio=miFormulario.cleaned_data['barrio'], id_sucursal=miFormulario.cleaned_data['id_sucursal']) 
                sucursal.save()                             
                return redirect('sucursales')                 
            else:
                return render(request, "AppGoldenCafe/sucursal.html", {'form': miFormulario})
            
        elif 'buscar_sucursal' in request.POST:
            miFormulario = sucursalFormulario()
            barrio = request.POST.get('barrio')
            if barrio:                       
                sucursales = Sucursal.objects.filter(barrio__iexact=barrio)
                if sucursales:
                    return render(request,"AppGoldenCafe/sucursal.html", {'sucursales': sucursales, 'barrio': barrio})
                else:
                    mensaje = "La sucursal ingresada no existe."
                    return render(request, "AppGoldenCafe/sucursal.html", {'mensaje': mensaje, 'form': miFormulario})
            else:
                mensaje = "Por favor, ingresa un barrio pedido para buscar la sucursal."
                return render(request, "AppGoldenCafe/sucursal.html", {'mensaje': mensaje, 'form': miFormulario})
            
        elif 'eliminar_sucursal' in request.POST:
            miFormulario = sucursalFormulario(request.POST)
            barrio = request.POST.get('barrio')
            if barrio:
                sucursal = Sucursal.objects.filter(barrio__iexact=barrio)
                if sucursal:
                   sucursal.delete()
                   return redirect('sucursales')
                else:
                    mensaje = "La sucursal o barrio ingresado no existe."
                    return render(request, "AppGoldenCafe/sucursal.html", {'mensaje': mensaje, 'form': miFormulario})   
            else:
                mensaje = "Por favor, ingresa un barrio para eliminar una sucursal"
                return render(request, "AppGoldenCafe/sucursal.html", {'mensaje': mensaje, 'form': miFormulario})

        else:
            miFormulario = sucursalFormulario()
            return render(request, "AppGoldenCafe/sucursal.html", {'form': miFormulario})
               
    else:                                                   
        miFormulario = sucursalFormulario()                  
        return render(request, "AppGoldenCafe/sucursal.html", {'sucursales': sucursales, 'form': miFormulario})

@login_required
def editar_sucursal(request, barrio):
    sucursal = Sucursal.objects.get(barrio=barrio)
    if request.method == 'POST':
        form = sucursalFormulario(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            return redirect('sucursales')
    else:
        form = sucursalFormulario(instance=sucursal)
        return render(request, 'AppGoldenCafe/editar_sucursal.html', {'form': form})

