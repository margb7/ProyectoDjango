from django.shortcuts import render
from .models import Cliente
from django.utils import timezone
# Create your views here.


def clientes_list(req):
    clientes = Cliente.objects.filter(alta__lte=timezone.now()).order_by('alta')
    return render(req, 'misitio/clientes_list.html', {'clientes': clientes})
