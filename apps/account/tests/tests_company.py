from apps.account.models import Company, CustomUser
from django.test import TestCase


class TestsCompanyModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.owner = CustomUser(
            email='teste@teste.com',
            first_name='Teste01',
            last_name='Last',
            is_staff=False,
            is_active=True,
        )
        cls.owner.save()

        cls.company = Company(owner=cls.owner, name='My Company')
        return super().setUpTestData()

    def test_insert_company(self):
        company = Company(owner=self.owner, name='company_test')
        company.save()
        assert company.pk

    def test_str_name_company(self):
        self.assertEqual(
            'pk {} -- Company {}'.format(self.company.pk, self.company.name),
            self.company.__str__())
