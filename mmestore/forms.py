from django import forms
from django.core.exceptions import ValidationError

import re


class ItemNumberForm(forms.Form):
    item_num = forms.CharField(label="Item Number", max_length=6)


class CategoryAddCraftItemForm(forms.Form):
    item_number = forms.CharField(label="Item Number", max_length=4)
    description = forms.CharField(label="Description", max_length=200)
    price = forms.FloatField(label="Price")
    shipping = forms.FloatField(label="Shipping Charge")
    width = forms.FloatField(label="Width", required=False)
    height = forms.FloatField(label="Height", required=False)
    depth = forms.FloatField(label="Depth", required=False)
    dress_size = forms.FloatField(label="Dress Size", required=False)

    def clean_item_number(self):
        data = self.cleaned_data["item_number"]
        p = re.compile(f"[A-Z0-9][0-9][0-9][0-9]$")
        if not p.match(data):
            raise ValidationError(
                ("Item number is not formatted correctly." "Please use default value."),
                code="invalid",
            )
        return data
