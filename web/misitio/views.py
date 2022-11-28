from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Cliente
from django.utils import timezone
from .forms import ClienteLogin


def clientes_list(req: HttpRequest):
    clientes = Cliente.objects.filter(alta__lte=timezone.now()).order_by('alta')
    return render(req, 'misitio/clientes_list.html', {'clientes': clientes})


def home_page(req: HttpRequest):
    return render(req, 'misitio/home_page.html')


def ventas_page(req: HttpRequest):
    return render(req, 'misitio/alquiler-venta.html')


def servicios_page(req: HttpRequest):
    return render(req, 'misitio/servicios.html')


def cuenta_page(req: HttpRequest):
    return render(req, 'misitio/cuenta.html')


def cliente_registro(req: HttpRequest):

    return render(req, 'misitio/login/registro.html')


def cliente_login(req: HttpRequest):

    if req.method == 'POST':

        form = ClienteLogin(req.POST)

        if form.is_valid():

            cliente = form.save(commit=False)
            cliente.save()

    else:

        form = ClienteLogin()

    return render(req, 'misitio/login/inicio_sesion.html', {'form': form})


def planes_page(req: HttpRequest):

    if req.method == "GET":

        return render(req, 'misitio/servicios/aplicar_planes.html', {'plan': req.GET.get("plan")})

    return render(req, 'misitio/servicios/aplicar_planes.html')
