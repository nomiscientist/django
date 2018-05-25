from django import template
from django.template import defaultfilters
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
def cut(value,arg):
    """ Removes all values of arg from the given string """
    return value.replace(arg,'')



@register.filter(name='lower', is_safe=True)
@defaultfilters.stringfilter
def lower(value):
    """Converts a string into all lowercase"""
    return value.lower()



@register.filter(needs_auoescape=True)
def initial_letter_filter(text,autoescape=None):
    """ Emphasize on first character """
    first, other=text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc=lambda x: x
    
    result='<strong>%s</strong>%s' %(esc(first), esc(other))
    return mark_safe(result)



@register.filter(expects_localtime=True)
def businesshours(value):
    try:
        return 9 <= value.hours < 17
    except ValueError:
        return ''



# register.filter('cut',cut)
# register.filter('lower',lower)

