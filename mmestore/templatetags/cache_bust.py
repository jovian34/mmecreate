import os
import uuid
from django import template

register = template.Library()


@register.simple_tag(name='cache_bust')
def cache_bust():

    if os.environ.get('DEVELOP'):
        version = uuid.uuid1()
    else:
        version = os.environ.get('PROJECT_VERSION')

    return f'__v__={version}'
