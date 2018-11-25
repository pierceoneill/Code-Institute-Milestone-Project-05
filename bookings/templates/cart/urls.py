from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', user_cart, name='cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^addplus/(?P<id>\d+)', add_plus, name='add_plus'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart')
]