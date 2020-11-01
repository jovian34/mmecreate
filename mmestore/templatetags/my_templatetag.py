from django import template

register = template.Library()


@register.filter(name='leading_zero_item_number')
def leading_zero_item_number(item_number: int) -> str:
    number_str = str(item_number)
    return number_str.zfill(4)
