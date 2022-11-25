from django.shortcuts import render
from .models import Cliente
from django.utils import timezone
from .forms import ClienteForm
# Create your views here.


def clientes_list(req):
    clientes = Cliente.objects.filter(alta__lte=timezone.now()).order_by('alta')
    return render(req, 'misitio/clientes_list.html', {'clientes': clientes})


def home_page(req):
    return render(req, 'misitio/home_page.html')


def ventas_page(req):
    return render(req, 'misitio/alquiler-venta.html')


def servicios_page(req):
    return render(req, 'misitio/servicios.html')


def cuenta_page(req):
    return render(req, 'misitio/cuenta.html')


def cliente_registro(req):

    return render(req, 'misitio/login/registro.html')

def cliente_login(req):

    if req.method == 'POST':

        form = ClienteForm(req.POST)

        if form.is_valid():

            cliente = form.save(commit=False)
            cliente.save()

    else:

        form = ClienteForm()

    return render(req, 'misitio/login/inicio_sesion.html', {'form': form})
