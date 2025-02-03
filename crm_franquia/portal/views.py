from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Unidade
from django.contrib import messages


def home(request):
    return render(request, 'portal/home.html')


# Dashboard do franqueado
@login_required
def dashboard_franqueado(request):
    if request.user.is_staff:
        # Administradores veem todas as unidades
        unidades = Unidade.objects.all()
    else:
        # Franqueados veem apenas suas unidades
        unidades = Unidade.objects.filter(usuarios=request.user)

    return render(request, 'portal/dashboard_franqueado.html', {'unidades': unidades})

@login_required
def editar_unidade(request, pk):

    unidade = get_object_or_404(Unidade, pk=pk, usuarios=request.user)
        # Alterna entre 'pendente' e 'ativa'
    if unidade.status == 'pendente':
        unidade.status = 'ativa'
    else:
        unidade.status = 'pendente'

    if request.method == 'POST':
        unidade.candidato = request.POST.get('candidato')
        unidade.contato_telefone = request.POST.get('contato_telefone')

        if 'anexo' in request.FILES:
            unidade.anexo = request.FILES['anexo']
        unidade.save()
        messages.success(request, f'Status da unidade "{unidade.unidade}" alterado para "{unidade.get_status_display()}".')
        return redirect('dashboard_franqueado')
    
    return render(request, 'portal/editar_unidade.html', {'unidade': unidade})

@login_required
def criar_unidade(request):
    if request.method == 'POST':
        # Criar a unidade
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        status = request.POST.get('status', 'pendente')

        unidade = Unidade.objects.create(nome=nome,endereco=endereco,telefone=telefone,status=status)

        # Associar o usuário logado (franqueado)
        unidade.usuarios.add(request.user)

        # Associar todos os administradores (staff)
        administradores = user.objects.filter(is_staff=True)
        unidade.usuarios.add(*administradores)

        return redirect('dashboard_franqueado')
    return render(request, 'portal/criar_unidade.html')