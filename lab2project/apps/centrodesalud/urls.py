from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from django.contrib.auth.views import logout, logout_then_login, login

from django.conf.urls import url
from lab2project.apps.centrodesalud.views import *


urlpatterns = [
    url(r'^$', index_view, name='url_index'),
    url(r'^login$', login,
        {'template_name': 'login.html'}, name='url_login'),
    url(r'^logout$', logout,
        {'template_name': 'index.html'}, name='url_logout'),

    url(r'^home$',login_required(home_view), name='url_home'),
    url(r'^cita_nueva$', login_required(CitaCreate.as_view()), name='url_createcita'),
    url(r'^miscitas$',login_required(CitaListar.as_view()), name='url_miscitas'),
    url(r'^cita/(?P<pk>\d+)/$', login_required(buscarPaciente3.as_view()), name='url_buscarpaciente'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(CitaUpdate.as_view()), name='url_edit'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(CitaDelete.as_view()), name='url_delete'),

    url(r'^clinica/nueva$', login_required(SucursalCreate.as_view()),name='url_createclinica'),
    url(r'^clinica/list$', login_required(SucursalListar.as_view()), name='url_clinicas'),
    url(r'^clinica/edit/(?P<pk>\d+)/$', login_required(SucursalUpdate.as_view()), name='url_editclinica'),
    url(r'^clinica/delete/(?P<pk>\d+)/$', login_required(SucursalDelete.as_view()), name='url_deleteclinica'),


]