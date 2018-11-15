from django.conf.urls import url, include
from .views import all_babysitters, babysitter_profile


urlpatterns = [
    url(r'^$', all_babysitters, name='babysitters'),
    url(r'^/(?P<id>\d+)/$', babysitter_profile, name='babysitter_profile'),
    ]