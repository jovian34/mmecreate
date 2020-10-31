from django.http import HttpResponse
from django.template import loader

from .models import Category


def index(request):
    template = loader.get_template('mmestore/index.html')
    return HttpResponse(template.render(request))


def categories(request):
    category_list = Category.objects.order_by('item_range_min')
    template = loader.get_template('mmestore/categories.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))


def category(request, category_id):
    category_item = Category.objects.get(pk=category_id)
    template = loader.get_template('mmestore/category.html')
    context = {
        'category_name': category_item.cat_name,
    }
    return HttpResponse(template.render(context, request))
