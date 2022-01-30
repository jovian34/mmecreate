from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path(f"category/<int:category_id>/", views.category, name="category"),
    path(
        f"category_add_craft_item/<int:category_id>/",
        views.category_add_craft_item,
        name="category_add_craft_item",
    ),
    path(f"craft_item/<item_number>/", views.craft_item, name="craft_item"),
    path(
        f"craft_item_ship/<item_number>/", views.craft_item_ship, name="craft_item_ship"
    ),
    path(f"item_lookup", views.item_lookup, name="item_lookup"),
    path(f"more_craft_fairs", views.more_craft_fairs, name="more_craft_fairs"),
    path(f"sold_at_fair/<fair_id>/", views.sold_at_fair, name="sold_at_fair"),
]
