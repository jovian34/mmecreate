from unittest import expectedFailure
from django.test import Client, TestCase
from django.db.utils import IntegrityError
from datetime import datetime, timedelta

from .models import CraftItem, Category, CraftFair


class CraftItemViewTests(TestCase):
    def setUp(self):
        self.c1 = Category.objects.create(cat_name="table runner", cat_code="2")
        self.c1.save()
        self.c2 = Category.objects.create(cat_name="hand bag", cat_code="A")
        self.c2.save()
        self.c3 = Category.objects.create(cat_name="pocket wallet", cat_code="0")
        self.c3.save()

        self.i1 = CraftItem.objects.create(
            category=self.c3,
            item_number="2001",
            price=8,
            shipping=4,
            description="fancy pink wallet",
        )
        self.i1.save()
        self.i2 = CraftItem.objects.create(
            category=self.c3,
            item_number="2002",
            price=9,
            shipping=5,
            description="fancy red wallet",
        )
        self.i2.save()
        self.i3 = CraftItem.objects.create(
            category=self.c3,
            item_number="2003",
            price=7,
            shipping=3,
            description="fancy blue wallet",
        )
        self.i3.save()
        self.i4 = CraftItem.objects.create(
            category=self.c2,
            item_number="1001",
            price=15,
            shipping=6,
            description="fancy purple hand bag",
        )
        self.i4.save()
        self.i5 = CraftItem.objects.create(
            category=self.c2,
            item_number="1002",
            price=14,
            shipping=5,
            has_it_been_sold=True,
            description="fancy olive hand bag",
        )
        self.i5.save()
        self.i6 = CraftItem.objects.create(
            category=self.c1,
            item_number="0001",
            price=22.5,
            shipping=9.25,
            description="fancy pink table runner",
        )
        self.i6.save()

        next_week = datetime.now() + timedelta(days=7)
        next_week_end = next_week + timedelta(hours=8)
        self.f1 = CraftFair.objects.create(
            fair_name="Tipton Pork Festival",
            fair_url="https:www.google.com",
            address="Downtown",
            city="Tipton",
            state="IN",
            first_start_time=next_week,
            first_end_time=next_week_end,
        )
        self.f1.save()

        last_week = datetime.now() + timedelta(days=-7)
        last_week_end = last_week + timedelta(hours=10)
        self.f2 = CraftFair.objects.create(
            fair_name="Atlanta Earth Festival",
            fair_url="https://www.visithamiltoncounty.com",
            address="PO Box",
            city="Atlanta",
            state="IN",
            first_start_time=last_week,
            first_end_time=last_week_end,
        )
        self.f2.save()

        two_hours_ago = datetime.now() + timedelta(hours=-2)
        two_hours_ago_end = two_hours_ago + timedelta(hours=5)
        self.f3 = CraftFair.objects.create(
            fair_name="IUK",
            fair_url="https:www.iuk.edu",
            address="2300 S Washington St",
            city="Kokomo",
            state="IN",
            first_start_time=two_hours_ago,
            first_end_time=two_hours_ago_end,
        )
        self.f3.save()

    def test_duplicate_item_raises_integrity_error(self):
        def create_dup_item_num():
            CraftItem.objects.create(
                category=self.c1,
                item_number="0001",
                description="fancy green table runner",
            )

        self.assertRaises(IntegrityError, create_dup_item_num)

    def test_item_lookup_page_renders(self):
        item_lookup_page_client = Client()
        response = item_lookup_page_client.get("/mmestore/item_lookup")
        contain_text = "Shop by item number:"
        self.assertContains(response, contain_text)
        self.assertIs(response.status_code, 200)

    def test_item_lookup_page_renders_fair(self):
        item_lookup_page_client = Client()
        response = item_lookup_page_client.get("/mmestore/item_lookup")
        contain_text = "IUK"
        self.assertContains(response, contain_text)
        self.assertIs(response.status_code, 200)

    def test_more_craft_fair_page_renders(self):
        item_lookup_page_client = Client()
        response = item_lookup_page_client.get("/mmestore/more_craft_fairs")
        contain_text = "Earth"
        self.assertContains(response, contain_text)
        self.assertIs(response.status_code, 200)

    def test_more_craft_fair_page_shows_today(self):
        item_lookup_page_client = Client()
        response = item_lookup_page_client.get("/mmestore/more_craft_fairs")
        contain_text = "IUK"
        self.assertContains(response, contain_text)
        self.assertIs(response.status_code, 200)

    def test_item_lookup_page_shows_fair_is_today(self):
        item_lookup_page_client = Client()
        response = item_lookup_page_client.get("/mmestore/item_lookup")
        contain_text = "Today - Come see us:"
        self.assertContains(response, contain_text)
        self.assertIs(response.status_code, 200)

    def test_categories_page_lists_items(self):
        categories_page_client = Client()
        response = categories_page_client.get("/mmestore/categories")
        self.assertEqual(response.status_code, 200)
        contain_text = "pocket wallet"
        self.assertContains(response, contain_text)

    def test_category_page_lists_items(self):
        cat_num = self.c3.pk
        category_page_client = Client()
        response = category_page_client.get(f"/mmestore/category/{cat_num}/")
        self.assertEqual(response.status_code, 200)
        contain_text = "fancy blue wallet"
        self.assertContains(response, contain_text)
        contain_text = "fancy pink wallet"
        self.assertContains(response, contain_text)
        contain_text = "fancy pink table runner"
        self.assertNotContains(response, contain_text)
        number_of_items = len(response.context["items"])
        self.assertIs(number_of_items, 3)

    def test_category_page_does_not_list_sold_items(self):
        cat_num = self.c2.pk
        category_page_sold_client = Client()
        response = category_page_sold_client.get(f"/mmestore/category/{cat_num}/")
        self.assertEqual(response.status_code, 200)
        contain_text = "fancy olive hand bag"
        self.assertNotContains(response, contain_text)
        contain_text = "fancy purple hand bag"
        self.assertContains(response, contain_text)
        number_of_items = len(response.context["items"])
        self.assertIs(number_of_items, 1)

    def test_craft_item_page_item(self):
        craft_item_page_item_client = Client()
        response = craft_item_page_item_client.get("/mmestore/craft_item/2002/")
        self.assertEqual(response.status_code, 200)
        contain_text = "fancy red wallet"
        self.assertContains(response, contain_text)
        contain_text = "pocket wallet"
        self.assertContains(response, contain_text)
        contain_text = "fancy pink wallet"
        self.assertNotContains(response, contain_text)

    def test_shipping_price_reported(self):
        shipping_price_client = Client()
        response = shipping_price_client.get("/mmestore/craft_item_ship/0001/")
        self.assertEqual(response.context["category_name"], "table runner")
        self.assertEqual(response.status_code, 200)
        shipping = response.context["ship_price"]
        self.assertEqual(shipping, 31.75)
        self.assertContains(response, "31.75")

    def test_miskeyed_item_number_raises_404(self):
        miskeyed_craft_item_page_item_client = Client()
        response = miskeyed_craft_item_page_item_client.get(
            "/mmestore/craft_item/4009/"
        )
        self.assertEqual(response.status_code, 404)

    def test_item_category(self):
        cat_num = self.c1.pk
        item = CraftItem.objects.get(item_number="0001")
        self.assertEqual(item.category.id, cat_num)

    @expectedFailure
    def test_category_add_craft_item_view(self):
        '''
        This is marked as expected failure until such a time as I can pass a logged in user
        as part of the setup in this test
        '''
        cat_num = self.c2.pk
        category_add_craft_item_client = Client()
        response = category_add_craft_item_client.post(
            f"/mmestore/category_add_craft_item/{cat_num}/",
            {
                "item_number": "A215",
                "description": "Bright red large",
                "price": "39.99",
                "shipping": "6",
                "width": "5",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CraftItem.objects.last().description, "Bright red large")
        self.assertEqual(CraftItem.objects.last().price, 39.99)

    def test_za_lookup_renders_with_no_future_craft_fairs(self):
        '''
        the za in the name forces the test to run after the other tests 
        due to it deleting f1 and f3 which are needed in prior tests
        '''

        self.f1.delete()
        self.f3.delete()
        item_lookup_page_client = Client()
        response = item_lookup_page_client.get("/mmestore/item_lookup")
        contain_text = "Shop by item number:"
        non_contain_text = "More Craft Fairs"
        self.assertContains(response, contain_text)
        self.assertNotContains(response, non_contain_text)
        self.assertIs(response.status_code, 200)

    def test_zb_more_craft_fair_renders_with_no_future_craft_fairs(self):
        '''
        This runs after test_za_lookup_renders_with_no_future_craft_fairs
        deleted all but the one past fair to show the page renders without
        a future fair
        '''
        self.test_more_craft_fair_page_renders