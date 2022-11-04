from django.shortcuts import render
from .models import Cliente
from django.utils import timezone
from .forms import ClienteForm
# Create your views here.


def clientes_list(req):
    clientes = Cliente.objects.filter(alta__lte=timezone.now()).order_by('alta')
    return render(req, 'misitio/clientes_list.html', {'clientes': clientes})


def cliente_new(req):

    if req.method == 'POST':

        form = ClienteForm(req.POST)

        if form.is_valid():

            cliente = form.save(commit=False)
            cliente.save()

    else:

        form = ClienteForm()

    return render(req, 'misitio/cliente_edit.html', {'form': form})
