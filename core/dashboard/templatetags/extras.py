# dashboard/templatetags/extras.py
import os
from django import template

register = template.Library()

@register.filter
def file_extension(value):
    if hasattr(value, 'name'):
        filename = value.name
    else:
        filename = str(value)
    return os.path.splitext(filename)[1][1:]