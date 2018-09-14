from django.template import Library
from django.urls import resolve

register = Library()


@register.simple_tag
def nav_active(request, url, style='active'):
    url_name = resolve(request.path).url_name
    if url_name in url.split('|'):
        return style
    return ''
