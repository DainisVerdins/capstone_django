from django.test import TestCase
import json
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
from django.urls import reverse
from django.contrib.auth.models import User 
from rest_framework.renderers import JSONRenderer

class MenuViewTest (TestCase):
    def setUp(self):
        menu_1 =Menu.objects.create(title="Soljanka", price=1.5,inventory=123)
        menu_2 =Menu.objects.create(title="Borch", price=2.5, inventory=321)

        menu_1.save()
        menu_2.save()
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')

        test_user1.save()
    
    def test_getall(self):
        menus = Menu.objects.all()
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('restaurant-menu'))

        serialized = MenuSerializer(menus, many=True)
        menus_json = JSONRenderer().render(serialized.data)
        self.assertEqual(menus_json, response.content)
