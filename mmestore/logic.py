from .models import Category, CraftItem


def get_next_craft_item_default(category_id):
    category = Category.objects.get(pk=category_id)
    cat_code = category.cat_code
    craft_items = CraftItem.objects.filter(category=category_id)
    id_list = [craft_item_obj.item_number for craft_item_obj in craft_items]
    for i in range(1, 1000):
        test_value = f"{cat_code}{i:03d}"
        if test_value not in id_list:
            return test_value
