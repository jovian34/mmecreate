from django.test import Client, TestCase
from django.db.utils import IntegrityError

from .models import CraftItem
from .models import Category


class CraftItemViewTests(TestCase):
    def setUp(self):
        self.table_runner = Category.objects.create(cat_name='table runner')
        self.hand_bag = Category.objects.create(cat_name='hand bag')
        self.pocket_wallet = Category.objects.create(cat_name='pocket wallet')
        CraftItem.objects.create(category=self.pocket_wallet, item_number='2001', description='fancy pink wallet')
        CraftItem.objects.create(category=self.pocket_wallet, item_number='2002', description='fancy red wallet')
        CraftItem.objects.create(category=self.pocket_wallet, item_number='2003', description='fancy blue wallet')
        CraftItem.objects.create(category=self.hand_bag, item_number='1001', description='fancy purple hand bag')
        CraftItem.objects.create(category=self.table_runner, item_number='0001', description='fancy pink table runner')

    def test_duplicate_item_raises_integrity_error(self):
        def create_dup_item_num():
            CraftItem.objects.create(category=self.table_runner,
                                     item_number='0001',
                                     description='fancy green table runner')
        self.assertRaises(IntegrityError, create_dup_item_num)

    def test_item_lookup_page_renders(self):
        item_lookup_page_client = Client()
        response = item_lookup_page_client.get('/mmestore/item_lookup')
        contain_text = 'enter 4 digital item ID'
        self.assertContains(response, contain_text)
        self.assertIs(response.status_code, 200)

    def test_category_page_lists_items(self):
        category_page_client = Client()
        response = category_page_client.get('/mmestore/category/3/')
        self.assertEqual(response.status_code, 200)
        contain_text = 'fancy blue wallet'
        self.assertContains(response, contain_text)
        contain_text = 'fancy pink wallet'
        self.assertContains(response, contain_text)
        contain_text = 'fancy pink table runner'
        self.assertNotContains(response, contain_text)
        number_of_items = len(response.context['items'])
        self.assertIs(number_of_items, 3)

    def test_craft_item_page_item(self):
        craft_item_page_item_client = Client()
        response = craft_item_page_item_client.get('/mmestore/craft_item/2002/')
        self.assertEqual(response.status_code, 200)
        contain_text = 'fancy red wallet'
        self.assertContains(response, contain_text)
        contain_text = 'pocket wallet'
        self.assertContains(response, contain_text)
        contain_text = 'fancy pink wallet'
        self.assertNotContains(response, contain_text)

    def test_miskeyed_item_number_raises_404(self):
        miskeyed_craft_item_page_item_client = Client()
        response = miskeyed_craft_item_page_item_client.get('/mmestore/craft_item/4009/')
        self.assertEqual(response.status_code, 404)










