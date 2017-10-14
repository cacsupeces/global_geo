from django.conf.urls import include, url
from django.contrib import admin
from geolocalisation.forms import LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import (index as site_index_view, sitemap as sitemap_view)
from contact import urls as contact_urls
from user import urls as user_urls
from .sitemaps import sitemaps as sitemaps_dict
from django.views.generic import (RedirectView, TemplateView)



admin.site.site_header = 'Géolocalisation Globale Admin'
admin.site.site_title = 'Géolocalisation Globale Site Admin'


urlpatterns = [
    # Examples:
    # url(r'^$', 'global_geo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(pattern_name='localisation_list', permanent=False)),
    url(r'^about/$', TemplateView.as_view(template_name='site/about.html'), name='about_site'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('geolocalisation.urls')),
    url(r'^contact/',	include(contact_urls)),
    url(r'^sitemap\.xml$', site_index_view, {'sitemaps': sitemaps_dict}, name='sitemap'),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap_view, {'sitemaps': sitemaps_dict}, name='sitemap-sections'),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^user/', include(user_urls, app_name='user', namespace='dj-auth')),
   
    
]
