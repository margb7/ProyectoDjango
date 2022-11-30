from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Cliente, Vinilo
from django.utils import timezone
from .forms import ClienteLogin


def clientes_list(req: HttpRequest):
    clientes = Cliente.objects.filter(alta__lte=timezone.now()).order_by('alta')
    return render(req, 'misitio/clientes_list.html', {'clientes': clientes})


def home_page(req: HttpRequest):

    vinilos = Vinilo.objects.filter().order_by("-ventas")

    return render(req, 'misitio/home_page.html', {'top_vinilos': vinilos})


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


def compra_page(req: HttpRequest):

    if req.method == "GET":

        if req.GET.get("album_id") != "":

            vinilo = Vinilo.objects.get(id=req.GET.get("album_id"))

            return render(req, 'misitio/compra_vinilo.html', {"vinilo": vinilo, "cantidad": -1, "email": ""})

        ## Error
        return render(req, 'misitio/compra_vinilo.html')

    elif req.method == "POST":

        vinilo = Vinilo.objects.get(id=req.POST.get("album_id"))
        cantidad = req.POST.get("cantidad")
        user_email = req.POST.get("user_email")

        return render(req, 'misitio/compra_vinilo.html', {"vinilo": vinilo, "cantidad": cantidad, "email": user_email})


    return render(req, 'misitio/compra_vinilo.html')