from django import template

register = template.Library()


def cut(value,arg):
    """ Removes all values of arg from the given string """
    return value.replace(arg,'')



@register.filter(name='lower')
def lower(value):
    """Converts a string into all lowercase"""
    return value.lower()

register.filter('cut',cut)
# register.filter('lower',lower)

