from django.contrib import admin
from django.db import models
from .models import Category, CraftItem, CraftFair


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("cat_name", "cat_code")


@admin.register(CraftItem)
class CraftItemAdmin(admin.ModelAdmin):
    model = CraftItem
    list_display = (
        "item_number",
        "category",
        "description",
        "price",
        "shipping",
        "has_it_been_sold",
        "photo_front",
    )
    search_fields = ["item_number"]


@admin.register(CraftFair)
class CraftFairAdmin(admin.ModelAdmin):
    model = CraftFair
    list_display = ("fair_name", "first_start_time")
