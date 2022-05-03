from django.test import TestCase

from crud.models import Company

# Create your tests here.

class CompanyCrudTest(TestCase):
    def setUp(self):
        Company.objects.create(
            name = "Test Company",
            address = "Dummy Address",
            phone = "2345678123",
            email = "test123@gmail.com",
            contract_type = "G",
        )

    def test_create(self):
        company = Company.objects.get(id=1)
        self.assertIsNotNone(company, 'Company instance created')

    def test_update(self):
        updated_name = "New Name"
        company = Company.objects.get(id=1)
        company.name = updated_name
        company.save()

        company = Company.objects.get(id=1)
        self.assertEqual(company.name, updated_name, "Company instance updated")

    def test_delete(self):
        company = Company.objects.get(id=1)
        company.delete()

        try:
            company = Company.objects.get(id=1)
        except Company.DoesNotExist:
            company = None

        self.assertIsNone(company, 'Company instance deleted')