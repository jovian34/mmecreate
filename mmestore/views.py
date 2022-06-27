from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .models import Category, CraftItem, CraftFair
from .forms import ItemNumberForm, CategoryAddCraftItemForm
from .viewlogic.fair_info import get_fair_details, sort_fairs
from .viewlogic.next_craft_item_number import get_next_craft_item_default


def index(request):
    return redirect("item_lookup")


class CategoriesListView(ListView):
    model = Category
    template_name = "mmestore/categories.html"
    ordering = "cat_name"


def category(request, category_id):
    category_item = get_object_or_404(Category, pk=category_id)
    craft_items = CraftItem.objects.filter(
        category=category_id, has_it_been_sold=False
    ).order_by("-item_number")
    context = {
        "category_name": category_item.cat_name,
        "category_id": category_id,
        "items": craft_items,
    }
    return render(request, "mmestore/category.html", context)


def craft_item(request, item_number):
    item = get_object_or_404(CraftItem, item_number=item_number)
    item_category = item.category.cat_name
    context = {
        "item": item,
        "category_name": item_category,
    }

    if item.has_it_been_sold:
        return render(request, "mmestore/craft_item_sold.html", context)

    return render(request, "mmestore/craft_item.html", context)


def craft_item_ship(request, item_number):
    item = get_object_or_404(CraftItem, item_number=item_number)
    if item.shipping:
        ship_price = item.price + item.shipping
    else:
        ship_price = item.price
    item_category = item.category.cat_name
    context = {
        "item": item,
        "category_name": item_category,
        "ship_price": ship_price,
    }
    return render(request, "mmestore/craft_item_ship.html", context)


def item_lookup(request):
    
    if request.method == "POST":
        form = ItemNumberForm(request.POST)
        if form.is_valid():
            item_num = form.cleaned_data["item_num"]
            return redirect("craft_item_ship", item_number=item_num)

    else:
        fair, fair_info = get_fair_details()        
        form = ItemNumberForm()
        context = {
            "fair": fair,
            "form": form,
            "fair_info": fair_info,
        }
        return render(request, "mmestore/item_lookup.html", context)


def more_craft_fairs(request):
    fairs_future, fairs_past, fair_in_progress = sort_fairs()
    context = {
        "fairs_future": fairs_future,
        "fairs_past": fairs_past,
        "fair_in_progress": fair_in_progress,
        "last_fair": fairs_past[0],
    }
    return render(request, "mmestore/more_craft_fairs.html", context)


def sold_at_fair(request, fair_id):
    fair = get_object_or_404(CraftFair, pk=fair_id)
    craft_items = CraftItem.objects.filter(
        craft_fair_id=fair_id, has_it_been_sold=True
    ).order_by("-item_number")
    context = {
        "fair": fair.__str__,
        "items": craft_items,
    }
    return render(request, "mmestore/sold_at_fair.html", context)


def category_add_craft_item(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == "POST":
        form = CategoryAddCraftItemForm(request.POST)
        if form.is_valid():
            add_item = CraftItem(
                category=category,
                item_number=form.cleaned_data["item_number"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
                shipping=form.cleaned_data["shipping"],
                width=form.cleaned_data["width"],
                height=form.cleaned_data["height"],
                depth=form.cleaned_data["depth"],
                dress_size=form.cleaned_data["dress_size"],
            )
            add_item.save()
        return redirect("item_lookup")
    else:
        id_default = get_next_craft_item_default(category_id)
        form = CategoryAddCraftItemForm(initial={"item_number": id_default})
        context = {
            "form": form,
            "category": category.cat_name,
        }
        return render(request, "mmestore/category_add_craft_item.html", context)
