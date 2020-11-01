from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.categories, name='categories'),
    path(f'category/<int:category_id>/', views.category, name='category'),
]
