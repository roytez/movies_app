from django import template

register = template.Library()


@register.filter
def is_true(value):
    if isinstance(value, str):
        value = value.lower()
    return value in [1, '1', 'true', True]


@register.filter
def subtract(value, arg):
    if isinstance(arg, str) and arg.isdigit():
        arg = int(arg)
    if isinstance(value, str) and value.isdigit():
        value = int(value)
    return value - arg
