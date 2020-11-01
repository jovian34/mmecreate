from django.shortcuts import get_object_or_404, render

from .models import Category


def index(request):
    return render(request, 'mmestore/index.html')


def categories(request):
    category_list = Category.objects.order_by('item_range_min')
    context = {
        'category_list': category_list,
    }
    return render(request, 'mmestore/categories.html', context)


def category(request, category_id):
    category_item = get_object_or_404(Category, pk=category_id)
    context = {
        'category_name': category_item.cat_name,
    }
    return render(request, 'mmestore/category.html', context)
