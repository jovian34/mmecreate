import pytest

from django.db.utils import IntegrityError

from ..models import Category, CraftItem, CraftFair

@pytest.fixture
def categories(client):
    t_run = Category.objects.create(cat_name="table runner", cat_code="2")
    h_bag = Category.objects.create(cat_name="hand bag", cat_code="A")
    p_wal = Category.objects.create(cat_name="pocket wallet", cat_code="0")
    return t_run, h_bag, p_wal

@pytest.fixture
def craft_items(client, categories):
    i2001 = CraftItem.objects.create(
            category=categories[2],
            item_number="2001",
            price=8,
            shipping=4,
            description="fancy pink wallet",
        )
    i2002 = CraftItem.objects.create(
            category=categories[2],
            item_number="2002",
            price=9,
            shipping=5,
            description="fancy red wallet",
        )
    i2003 = CraftItem.objects.create(
            category=categories[2],
            item_number="2003",
            price=7,
            shipping=3,
            description="fancy blue wallet",
        )
    i1001 = CraftItem.objects.create(
            category=categories[1],
            item_number="1001",
            price=15,
            shipping=6,
            description="fancy purple hand bag",
        )
    i1002 = CraftItem.objects.create(
            category=categories[2],
            item_number="1002",
            price=14,
            shipping=5,
            has_it_been_sold=True,
            description="fancy olive hand bag",
        )
    i0001 = CraftItem.objects.create(
            category=categories[0],
            item_number="0001",
            price=22.5,
            shipping=9.25,
            description="fancy pink table runner",
        )
    return i2001, i2002, i2003, i1001, i1002, i0001
        

@pytest.mark.django_db
def test_duplicate_item_raises_integrity_error(client, categories, craft_items):
    with pytest.raises(IntegrityError) as execinfo:
        test_item = CraftItem.objects.create(
                    category=categories[0],
                    item_number="0001",
                    description="fancy green table runner",
                )
    assert "duplicate key value violates unique constraint" in str(execinfo.value) 