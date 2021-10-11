from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    if int(num) % int(val) == 0:
        return 0
    else:
         return 1