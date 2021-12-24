from django import forms


class ItemNumberForm(forms.Form):
    item_num = forms.CharField(label='Item Number', max_length=6)


class CategoryAddCraftItemForm(forms.Form):
    item_num = forms.CharField(label='Item Number', max_length=4)
    description = forms.CharField(label='Description', max_length=200)
    price = forms.FloatField(label="Price")
    shipping = forms.FloatField(label="Shipping Charge")
    width = forms.FloatField(label="Width")
    height = forms.FloatField(label="Height")
    depth = forms.FloatField(label="Depth")
    dress_size = forms.FloatField(label="Dress Size")
    
