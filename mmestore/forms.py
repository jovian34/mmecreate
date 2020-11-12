from django import forms


class ItemNumberForm(forms.Form):
    item_num = forms.CharField(label='Item Number', max_length=6)
