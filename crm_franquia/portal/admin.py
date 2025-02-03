from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Unidade

# Exibir informações adicionais no admin de usuários
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

# Substituir o admin padrão de usuários
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Admin para Unidades
@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    # Campos exibidos apenas para admins
    list_display = ('unidade', 'uf', 'candidato', 'primeira_meeting_status', 'status')

    # Filtros
    list_filter = ('unidade', 'uf', 'status')
    search_fields = ('unidade', 'candidato', 'email_candidato')
    ordering = ('unidade',)

    def save_model(self, request, obj, form, change):
        # Salva a unidade
        super().save_model(request, obj, form, change)

        # Associa o usuário logado (franqueado) à unidade
        if not change:  # Apenas para novas unidades
            obj.usuarios.add(request.user)

        # Associa todos os administradores (staff) à unidade
        administradores = User.objects.filter(is_staff=True)
        obj.usuarios.add(*administradores)