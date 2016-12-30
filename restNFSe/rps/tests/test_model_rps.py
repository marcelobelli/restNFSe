from django.test import TestCase

from model_mommy import mommy

from ..models import RPS
from restNFSe.accounts.models import User


class RPSModelTest(TestCase):
    def setUp(self):
        self.rps = mommy.make(RPS)

    def test_create(self):
        self.assertTrue(RPS.objects.exists())