"""minderfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.contrib import admin
from home.views import get_index
from blog.views import PostListView
from accounts import urls as urls_accounts
from babysitters import urls as urls_babysitters
from babysitters.views import all_babysitters
from blog import urls as urls_blog
from bookings import urls as urls_bookings
from search import urls as urls_search
from checkout import urls as urls_checkout
from about import urls as urls_about
from contact import urls as urls_contact
from django.views import static
from django.contrib.auth import views
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^babysitters/', include(urls_babysitters)),
    url(r'^bookings/', include(urls_bookings)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^blog/', include(urls_blog)),
    url(r'^about/', include(urls_about)),
    url(r'^contact/', include(urls_contact))
]
