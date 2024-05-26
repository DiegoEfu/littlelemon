from django.test import TestCase, Client

from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setup(self) -> None:
        MenuItem.objects.create(title="Dish1", price=15, inventory=500)
        MenuItem.objects.create(title="Dish2", price=25, inventory=50)
        MenuItem.objects.create(title="Dish3", price=150, inventory=5)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)		