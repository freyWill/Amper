from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    try:
        result = dictionary.get(key)
    except Exception:
        result = ""
    return result
