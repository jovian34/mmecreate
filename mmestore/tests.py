from django.test import TestCase

from .models import CraftItem


class CraftItemModelTests(TestCase):

    def test_new_craft_item_has_unique_id(self):
        item_one = CraftItem(category=1, item_number='0003', price=15)
        item_two = CraftItem(category=2, item_number='0003', price=20)




