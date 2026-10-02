from django.test import TestCase
from .models import Currency, Warehouse, Supplier
from users.models import Business

class CommerceModelTests(TestCase):
    def setUp(self): self.business=Business.objects.create(name="Test Business")
    def test_currency_and_warehouse_are_business_scoped(self):
        Currency.objects.create(business=self.business,code="NGN",name="Nigerian Naira",symbol="₦")
        Warehouse.objects.create(business=self.business,name="Main Warehouse",code="MAIN")
        Supplier.objects.create(business=self.business,name="Test Supplier")
        self.assertEqual(self.business.currencies.count(),1)
        self.assertEqual(self.business.warehouses.count(),1)
        self.assertEqual(self.business.suppliers.count(),1)
