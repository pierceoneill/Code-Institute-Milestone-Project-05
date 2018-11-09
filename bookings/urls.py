from django.conf.urls import url
from .views import view_bookings, add_to_bookings, adjust_bookings

urlpatterns = [
    url(r'^$', view_bookings, name='view_bookings'),
    url(r'^add/(?P<id>\d+)', add_to_bookings, name='add_to_bookings'),
    url(r'^adjust/(?P<id>\d+)', adjust_bookings, name='adjust_bookings'),
    ]