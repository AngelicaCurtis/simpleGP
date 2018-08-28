from django import template

register = template.Library()

@register.simple_tag
def contador(valor):
    return valor+1(valor)