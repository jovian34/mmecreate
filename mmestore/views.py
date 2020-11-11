from django.shortcuts import get_object_or_404, render

from .models import Category, CraftItem


def index(request):
    return render(request, 'mmestore/index.html')


def categories(request):
    category_list = Category.objects.order_by('cat_name')
    context = {
        'category_list': category_list,
    }
    return render(request, 'mmestore/categories.html', context)


def category(request, category_id):
    category_item = get_object_or_404(Category, pk=category_id)
    craft_items = CraftItem.objects.filter(category=category_id).order_by('-item_number')
    context = {
        'category_name': category_item.cat_name,
        'items': craft_items,
    }
    return render(request, 'mmestore/category.html', context)


def craft_item(request, item_number):
    item = get_object_or_404(CraftItem, item_number=item_number)
    item_category = item.category.cat_name
    context = {
        'item': item,
        'category_name': item_category,
    }
    return render(request, 'mmestore/craft_item.html', context)


def item_lookup(request):
    pass


def construction(request):
    return render(request, 'mmestore/construction.html')

