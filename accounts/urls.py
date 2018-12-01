from django.conf.urls import url, include
from .views import register, profile, logout, login, update_profile, update_profile_kid, create_profile_kid, delete_profile_kid
from accounts import url_reset

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/update/$', update_profile, name='update_profile'),
    url(r'^profile/kids/update/(?P<id>\d+)$', update_profile_kid, name='update_profile_kid'),
    url(r'^profile/kids/delete/(?P<id>\d+)$', delete_profile_kid, name='delete_profile_kid'),
    url(r'^profile/kids/create/$', create_profile_kid, name='create_profile_kid'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login', login, name='login'),
    url(r'^password-reset/', include(url_reset))
]