from django.contrib import admin
from .models import Category, CraftItem

admin.site.register(Category)


@admin.register(CraftItem)
class CraftItemAdmin(admin.ModelAdmin):
    model = CraftItem
    list_display = ('item_number', 'category', 'description')
    search_fields = ['item_number']
