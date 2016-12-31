import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .managers import CustomUserManager
from restNFSe.utils.to_dict import dict_prestador


_cert_storage = FileSystemStorage(location=os.path.join(settings.BASE_DIR,
                                                        'restNFSe',
                                                        'account',
                                                        'cert'))


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    razao_social = models.CharField('Razão Social', max_length=100, unique=True)
    cnpj = models.CharField('CNPJ', max_length=14, unique=True)
    inscricao_municipal = models.CharField('Inscrição Municipal', max_length=20)
    codigo_municipio = models.CharField('Código do Município', max_length=7)


    producao = models.BooleanField('Produção', default=False,
                                   help_text='Define se as requisições serão '
                                             'realizadas no servidor de produção')
    certificado_pfx = models.FileField(verbose_name='Certificado PFX',
                                       storage=_cert_storage, null=True, blank=True)
    senha_certificado = models.CharField('Senha Certificado', max_length=20, blank=True)

    numero_lote_rps = models.IntegerField('Número Lote RPS', default=1)

    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=False)
    date_joined = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.email

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(' ')[0]

    def get_numero_lote(self):
        self.numero_lote_rps = models.F('numero_lote_rps') + 1
        self.save(update_fields=['numero_lote_rps'])
        self.refresh_from_db()
        return self.numero_lote_rps

    def to_dict(self):
        return dict_prestador(self)
