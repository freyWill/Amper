from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key): # custom template tag that converts product title to the value of available items in the cart
    try:
        result = dictionary.get(key)
    except Exception:
        result = ""
    return result

@register.filter
def range( value ):
  return range( value )