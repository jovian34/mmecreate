import pytest

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.utils import timezone
from datetime import timedelta

from ..models import Category, CraftItem, CraftFair
from .fixture_views import categories, craft_items, fairs


@pytest.mark.django_db
def test_duplicate_item_raises_integrity_error(client, categories, craft_items):
    with pytest.raises(IntegrityError) as execinfo:
        test_item = CraftItem.objects.create(
                    category=categories[0],
                    item_number="0001",
                    description="fancy green table runner",
                )
    assert "duplicate key value violates unique constraint" in str(execinfo.value)

@pytest.mark.django_db
def test_item_lookup_page_renders(client, categories, craft_items, fairs):
    response = client.get("/mmestore/item_lookup")
    assert "Shop by item number:" in str(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_item_lookup_page_renders_fair(client, categories, craft_items, fairs):
    response = client.get("/mmestore/item_lookup")
    assert "IUK" in str(response.content)

@pytest.mark.django_db
def test_more_craft_fair_page_renders(client, categories, craft_items, fairs):
    response = client.get("/mmestore/more_craft_fairs")
    assert "Earth" in str(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_more_craft_fair_page_shows_today(client, categories, craft_items, fairs):
    response = client.get("/mmestore/more_craft_fairs")
    assert "Downtown" in str(response.content)

@pytest.mark.django_db
def test_item_lookup_page_shows_fair_is_today(client, categories, craft_items, fairs):
    response = client.get("/mmestore/item_lookup")
    assert "Today - Come see us:" in str(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_categories_page_lists_items(client, categories, craft_items, fairs):
    response = client.get("/mmestore/categories")
    assert "pocket wallet" in str(response.content)
    assert response.status_code == 200

@pytest.mark.django_db
def test_category_page_lists_items(client, categories, craft_items, fairs):
    response = client.get(f"/mmestore/category/{categories[2].pk}/", follow=True)
    assert response.status_code == 200
    assert "fancy blue wallet" in str(response.content)
    assert "fancy pink wallet" in str(response.content)
    assert "fancy pink table runner" not in str(response.content)
    assert len(response.context["items"]) == 3

@pytest.mark.django_db
def test_category_page_does_not_list_sold_items(client, categories, craft_items, fairs):
    response = client.get(f"/mmestore/category/{categories[1].pk}/", follow=True)
    assert response.status_code == 200
    assert "fancy olive hand bag" not in str(response.content)
    assert "fancy purple hand bag" in str(response.content)
    assert len(response.context["items"]) == 1

@pytest.mark.django_db
def test_craft_item_page_renders_only_correct_item(client, categories, craft_items, fairs):
    response = client.get("/mmestore/craft_item/2002/")
    assert response.status_code == 200
    assert "fancy red wallet" in str(response.content)
    assert "2002" in str(response.content)
    assert "fancy pink wallet" not in str(response.content)

@pytest.mark.django_db
def test_shipping_price_reported(client, categories, craft_items, fairs):
    response = client.get("/mmestore/craft_item_ship/0001/")
    assert response.status_code == 200
    assert "table runner" == response.context["category_name"]
    assert 31.75 == response.context["ship_price"]
    assert "31.75" in str(response.content)

@pytest.mark.django_db
def test_miskeyed_item_number_raises_404(client, categories, craft_items, fairs):
    response = client.get("/mmestore/craft_item/4009/")
    assert response.status_code == 404

@pytest.mark.django_db
def test_item_category(categories, craft_items):
    item = CraftItem.objects.get(item_number="0001")
    assert item.category.id == categories[0].pk

@pytest.fixture
def logged_user_balius(client):
    user = User.objects.create_user(
        username="balius",
        email="balius@jovian34.com",
        password="Hdbwrwbrj7239293skjhkasH72!",
        first_name="Balius",
    )
    client.login(username="balius", password="Hdbwrwbrj7239293skjhkasH72!")
    return user

@pytest.mark.django_db
def test_category_add_craft_item_view_logged_in(client, categories, craft_items, fairs, logged_user_balius):
    response = client.post(
        f"/mmestore/category_add_craft_item/{categories[1].pk}/",
        {
            "item_number": "A215",
            "description": "Bright red large",
            "price": "39.99",
            "shipping": "6",
            "width": "5",
        },
    )
    assert response.status_code == 302
    assert "Bright red large" == CraftItem.objects.last().description
    assert 39.99 == CraftItem.objects.last().price


@pytest.mark.django_db
def test_item_lookup_page_renders_logged_in(client, categories, craft_items, fairs, logged_user_balius):
    response = client.get("/mmestore/item_lookup")
    assert "Welcome, Balius" in str(response.content)

@pytest.mark.django_db
def test_category_add_craft_item_view_not_logged_in(client, categories, craft_items, fairs):
    response = client.post(
        f"/mmestore/category_add_craft_item/{categories[1].pk}/",
        {
            "item_number": "A215",
            "description": "Bright red large",
            "price": "39.99",
            "shipping": "6",
            "width": "5",
        },
    )
    assert response.status_code == 302
    assert "fancy pink table runner" == CraftItem.objects.last().description
    assert 22.5 == CraftItem.objects.last().price

@pytest.mark.django_db
def test_item_lookup_page_renders_login_button_not_logged_in(client, categories, craft_items, fairs):
    response = client.get("/mmestore/item_lookup")
    assert "Staff login" in str(response.content)

@pytest.mark.django_db
def test_lookup_renders_with_no_future_craft_fairs(client, categories, craft_items, fairs):
    fairs[0].delete()
    fairs[2].delete()
    response = client.get("/mmestore/item_lookup")
    assert response.status_code == 200
    assert "Shop by item number:" in str(response.content)
    assert "More Craft Fairs" not in str(response.content)

@pytest.mark.django_db
def test_more_craft_fair_renders_with_no_future_craft_fairs(client, categories, craft_items, fairs):
    fairs[0].delete()
    fairs[2].delete()
    response = client.get("/mmestore/more_craft_fairs")
    assert "Earth" in str(response.content)
    assert response.status_code == 200