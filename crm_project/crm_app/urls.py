from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:pk>/', views.detalhes_cliente, name='detalhes_cliente'),
    path('cliente/novo/', views.novo_cliente, name='novo_cliente'),
    path('cliente/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('cliente/<int:pk>/excluir/', views.excluir_cliente, name='excluir_cliente'),
]