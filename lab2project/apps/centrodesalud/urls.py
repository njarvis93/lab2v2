from django.conf.urls import url, include


from django.contrib.auth.views import logout, logout_then_login, login

from django.conf.urls import url
from lab2project.apps.centrodesalud.views import *



urlpatterns = [
    url(r'^$', index_view, name='url_index'),
    url(r'^login$', login,
        {'template_name': 'login.html'}, name='url_login'),
url(r'^home$', home_view, name='url_home'),
]