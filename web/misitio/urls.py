from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('cliente/login/', views.cliente_login, name='login_page'),
    path('cliente/registro/', views.cliente_registro, name='register_page'),
    path('ventas', views.ventas_page, name="ventas_page"),
    path('servicios', views.servicios_page, name="servicios_page"),
    path('cuenta', views.cuenta_page, name="cuenta_page"),
    path('servicios/planes', views.planes_page, name="planes_page")
]
