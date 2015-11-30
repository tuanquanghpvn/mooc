from django import template

register = template.Library()


@register.filter
def minfilter(num):
    return int(num - 4)


@register.filter
def maxfilter(num):
    return int(num + 4)
