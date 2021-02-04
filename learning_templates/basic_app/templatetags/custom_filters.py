from django import template

register = template.Library()

@register.filter(name='customcut')
def customcut(value,arg):
    """
    This cuts out all values of "arg" from the string (assumed)
    """
    return value.replace(arg,'')

# register.filter('customcut',customcut)
