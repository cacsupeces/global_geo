from django.conf.urls import url
from .views import (LocalisationDetail, LocalisationList, LocalisationCreate, LocalisationUpdate, LocalisationDelete, IdentiteList, IdentiteCreate, IdentiteDetail, IdentiteUpdate, IdentiteDelete)
from .feeds import (AtomLocalisationFeed, Rss2LocalisationFeed)

urlpatterns = [
	url(r'^localisation/$', LocalisationList.as_view(), name='localisation_list'),
	url(r'^localisation/create/$', LocalisationCreate.as_view(), name='localisation_create'),
	url(r'^(?P<localisation_pk>[0-9]+)/atom/$', AtomLocalisationFeed(), name='localisation_atom_feed'),
	url(r'^(?P<localisation_pk>[0-9]+)/rss/$', Rss2LocalisationFeed(), name='localisation_rss_feed'),
	url(r'^localisation/(?P<pk>[0-9]+)/update/$', LocalisationUpdate.as_view(), name='localisation_update'),
	url(r'^localisation/(?P<pk>[0-9]+)/delete/$', LocalisationDelete.as_view(), name='localisation_delete'),
	url(r'^localisation/(?P<pk>[0-9]+)/$',LocalisationDetail.as_view(), name='localisation_detail'),
	url(r'^identite/$', IdentiteList.as_view(), name='identite_list'),
	url(r'^identite/create/$', IdentiteCreate.as_view(), name='identite_create'),
	url(r'^identite/(?P<pk>[0-9]+)/update/$', IdentiteUpdate.as_view(), name='identite_update'),
	url(r'^identite/(?P<pk>[0-9]+)/delete/$', IdentiteDelete.as_view(), name='identite_delete'),
	url(r'^identite/(?P<pk>[0-9]+)/$', IdentiteDetail.as_view(), name='identite_detail'),
	
	
	
	
	
]




