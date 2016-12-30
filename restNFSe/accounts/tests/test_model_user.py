from django.test import TestCase

from ..models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User(
            email='teste@teste.com',
            name='Teste da Silva',
            razao_social='Teste Corp',
            cnpj='12345678901234',
            inscricao_municipal='0987654321',
            codigo_municipio='1234567'
        )
        self.user.save()

    def test_create(self):
        self.assertTrue(User.objects.exists())