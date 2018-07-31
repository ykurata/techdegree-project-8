from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mineral_list, name='list'),
    url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'search/$', views.search, name="search"),
    url(r'random/$', views.random_mineral, name='random'),
    url(r'search/(?P<letter>[A-Z])$', views.search_by_letter, name="alphabet"),
    url(r'group/(?P<group>[\w\s]+)/$', views.search_by_group, name='group'),
]
