from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.categories, name='categories'),
    path(f'category/<int:category_id>/', views.category, name='category'),
    path(f'craft_item/<int:item_number>/', views.craft_item, name='craft_item'),
]
