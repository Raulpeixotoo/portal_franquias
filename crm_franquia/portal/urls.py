from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home_page
    path('dashboard/', views.dashboard_franqueado, name='dashboard_franqueado'),
    path('unidade/<int:pk>/editar/', views.editar_unidade, name='editar_unidade'),
]