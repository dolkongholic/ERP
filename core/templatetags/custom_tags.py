# post_extras.py
from django import template

register = template.Library()

@register.filter
def multiple(value,arg):
    return value * arg