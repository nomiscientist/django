from django import template
import datetime
from books.models import Book


register = template.Library()


# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)

# @register.simple_tag(takes_context=True)
# def current_time_with_context(context, format_string):
#     timezone = context['timezone']
#     return your_get_current_time_method(timezone, format_string)

# @register.simple_tag(lambda x: x-1, name="minusone")

# @register.simple_tag(name="minustwo")
# def some_function(value):
#     return value - 2



# def my_tag(a,b,*args,**kwargs):
#     warning=kwargs['warning']
#     profile=kwargs['profile']
#     return pass



# def books_for_author(author):
#     books = Book.objects.filter(authors__id=author.id)
#     return {'books':books}


@register.assignment_tag
def get_current_time(format_string):
    return datetime.datetime.now().strftime(format_string)



