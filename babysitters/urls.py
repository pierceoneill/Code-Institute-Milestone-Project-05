from django.conf.urls import url, include
from .views import all_babysitters, babysitter_profile, search


urlpatterns = [
    url(r'^$', all_babysitters, name='babysitters'),
    url(r'^babysitter_profile/(?P<id>\d+)/$', babysitter_profile, name='babysitter_profile'),
    url(r'^search/$', search, name='search'),
]
