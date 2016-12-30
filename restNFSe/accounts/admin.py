from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserAdminCreationForm, UserAdminForm


class CustomUserAdmin(UserAdmin):

    add_form = UserAdminCreationForm
    add_fieldsets = (
        (
            'Informações do Usuário', {
                'fields': (
                    'email',
                    'name',
                    'password1',
                    'password2',
                )
            }
        ),
        (
            'Informações da Empresa', {
                'fields': (
                    'razao_social',
                    'cnpj',
                    'inscricao_municipal',
                    'codigo_municipio',
                )
            }
        ),
    )

    form = UserAdminForm
    fieldsets = (
        (
            'Informações do Usuário', {
                'fields': (
                    ('email', 'name'),
                )
            }
        ),
        (
            'Informações da Empresa', {
                'fields': (
                    ('razao_social', 'cnpj'),
                    ('inscricao_municipal', 'codigo_municipio'),
                )
            }
        ),
        (
            'Certificado', {
                'fields': (
                    'producao',
                    'certificado_pfx',
                    'senha_certificado',
                    'numero_lote_rps',
                )
            }
        ),
        (
            'Permissões', {
                'classes': ('collapse',),
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                    'date_joined',
                    'last_login',
                )
            }
        ),
    )
    readonly_fields = ['date_joined', 'last_login']
    list_display = ['email', 'name', 'is_active', 'is_staff', 'date_joined']
    ordering = ['email']


admin.site.register(User, CustomUserAdmin)
