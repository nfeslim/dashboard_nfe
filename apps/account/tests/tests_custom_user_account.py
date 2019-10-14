from django.test import TestCase

from apps.account.models import CustomUser


class TestsCustomUserModel(TestCase):
    def setUp(self):
        self.data_insert = {
            'email': 'teste@teste.com',
            'first_name': 'Teste01',
            'last_name': 'Last',
            'is_staff': False,
            'is_active': True,
            'notes': 'Teste de Notes',
        }

    def test_insert_custom_user(self):
        user = CustomUser.objects.create(
            email=self.data_insert.get('email'),
            first_name=self.data_insert.get('first_name'),
            last_name=self.data_insert.get('last_name'),
            is_staff=self.data_insert.get('is_staff'),
            is_active=self.data_insert.get('is_active'),
            notes=self.data_insert.get('notes'),
        )

        self.assertIsNotNone(user.pk)
