from django.shortcuts import render
from .models import Mesa, Pedido, Plato

def mostrar_menu(request):
    platos = Plato.objects.all()
    return render(request, 'menu.html', {'platos': platos})

def tomar_pedido(request, mesa_id):
    mesa = Mesa.objects.get(id=mesa_id)
    platos = Plato.objects.all()
    
    if request.method == 'POST':
        platos_seleccionados = request.POST.getlist('platos')
        pedido = Pedido.objects.create(mesa=mesa)
        pedido.platos.set(platos_seleccionados)
        return render(request, 'confirmacion_pedido.html', {'pedido': pedido})
    
    return render(request, 'tomar_pedido.html', {'mesa': mesa, 'platos': platos})

def gestionar_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'gestionar_mesas.html', {'mesas': mesas})

