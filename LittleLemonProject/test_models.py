from django.test import TestCase
from FirstApp.models import Menu

class Menutest(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(title="IceCream",price="80",inventry=100)
        itemstr=item.get_item()
        self.assertEqual(itemstr,"IceCream:80")