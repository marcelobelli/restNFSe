from datetime import datetime

from django.test import TestCase

from model_mommy import mommy

from ..models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = mommy.make(User)

    def test_create(self):
        self.assertTrue(User.objects.exists())

    def test_email_unique(self):
        field = User._meta.get_field('email')
        self.assertTrue(field.unique)

    def test_razao_social_unique(self):
        field = User._meta.get_field('razao_social')
        self.assertTrue(field.unique)

    def test_cnpj_unique(self):
        field = User._meta.get_field('cnpj')
        self.assertTrue(field.unique)

    def test_date_joined(self):
        self.assertIsInstance(self.user.date_joined, datetime)

    def test_is_staff_default_to_False(self):
        self.assertEqual(self.user.is_staff, False)

    def test_is_active_default_to_False(self):
        self.assertEqual(self.user.is_active, False)

    def test_is_superuser_default_to_False(self):
        self.assertEqual(self.user.is_superuser, False)