from django.template import Library

register = Library()


def contador(valor):
    return valor + 1


register.filter("contador", contador)
