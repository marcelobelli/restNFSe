from django.test import TestCase

from model_mommy import mommy

from ..models import RPS
from restNFSe.accounts.models import User


class RPSModelTest(TestCase):
    def setUp(self):
        self.rps = mommy.make(RPS)

    def test_create(self):
        self.assertTrue(RPS.objects.exists())

    def test_numero_lote_exists(self):
        self.assertTrue(self.rps.numero_lote)

    def test_se_numero_lote_e_igual_no_usuario(self):
        numero_lote_user = User.objects.values_list('numero_lote_rps', flat=True).get(id=self.rps.prestador_id)
        self.assertEqual(self.rps.numero_lote, numero_lote_user)
