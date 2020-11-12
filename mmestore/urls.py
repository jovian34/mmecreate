from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.categories, name='categories'),
    path(f'category/<int:category_id>/', views.category, name='category'),
    path(f'craft_item/<item_number>/', views.craft_item, name='craft_item'),
    path(f'craft_item_ship/<item_number>/', views.craft_item_ship, name='craft_item_ship'),
    path(f'construction', views.construction, name='construction'),
    path(f'item_lookup', views.item_lookup, name='item_lookup'),
]
