from django.shortcuts import render
from django.template import Template, Context
import datetime
from django.http import HttpResponse

# Create your views here.
# def order(request):
#     t = Template("siteapp/order.html")
#     c = Context({'person_name': 'John Smith','company': 'Outdoor Equipment',
#                  'ship_date': datetime.date(2017, 7, 2),'ordered_warranty': False})
    
#     return HttpResponse(request,)

def order(request):
    t = "siteapp/order.html"
    c = {'person_name': 'John Smith','company': 'Outdoor Equipment',
                 'ship_date': datetime.date(2017, 7, 2),'ordered_warranty': False}
    
    return render(request,t,c)

class SilentAssertionError(Exception):
    silent_variable_failure = True

class Person(object):
    
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name

    def get_first_name(self):
        # raise AssertionError("foo")
        raise SilentAssertionError


def test(request):
    t = "siteapp/test.html"
    # person = {'name': 'Sally', 'age': '43'}
    # c = {'person': person}
    # c = {'person': Person('John', 'Smith')}
    # items = ['apples', 'bananas', 'carrots']
    p = Person('John', 'Smith')
    c = {"person": p}
    return render(request,t,c)


    

    
