import datetime
from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag(name='this_year')
def this_year():
    current = datetime.now()
    return current.year