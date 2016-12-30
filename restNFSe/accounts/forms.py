from django.forms import ModelForm
from django.contrib.auth.admin import UserCreationForm

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'razao_social',
            'cnpj',
            'inscricao_municipal',
            'codigo_municipio'
        ]


class UserAdminForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'razao_social',
            'cnpj',
            'inscricao_municipal',
            'codigo_municipio',
            'producao',
            'certificado_pfx',
            'senha_certificado',
            'is_active',
            'is_staff',
            'numero_lote_rps',
        ]
