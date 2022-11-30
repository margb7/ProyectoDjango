import re
from django import template

register = template.Library()


@register.simple_tag
def mult(a, b):

    val = float(a) * float(b)

    return val
