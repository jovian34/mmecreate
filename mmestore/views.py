from django.shortcuts import get_object_or_404, render, redirect

from .models import Category, CraftItem
from .forms import ItemNumberForm


def index(request):
    # return render(request, 'mmestore/index.html')
    return redirect('item_lookup') # for Artie FEST


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

    if item.has_it_been_sold:
        return render(request, 'mmestore/craft_item_sold.html', context)

    return render(request, 'mmestore/craft_item.html', context)


def craft_item_ship(request, item_number):
    item = get_object_or_404(CraftItem, item_number=item_number)
    if item.shipping:
        ship_price = item.price + item.shipping
    else:
        ship_price = item.price
    item_category = item.category.cat_name
    context = {
        'item': item,
        'category_name': item_category,
        'ship_price': ship_price,
    }
    return render(request, 'mmestore/craft_item_ship.html', context)


def construction(request):
    return render(request, 'mmestore/construction.html')


def item_lookup(request):
    if request.method == 'POST':
        form = ItemNumberForm(request.POST)
        if form.is_valid():
            item_num = form.cleaned_data['item_num']
            return redirect('craft_item', item_number=item_num)
    else:
        form = ItemNumberForm()
        return render(request, 'mmestore/item_lookup.html', {'form': form})
