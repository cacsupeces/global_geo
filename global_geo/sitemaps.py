from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


from geolocalisation.sitemaps import (LocalisationSitemap, IdentiteSitemap)


class RootSitemap(Sitemap):
    priority = 0.6

    def items(self):
        return [
            'about_site',
            'contact',
            'dj_auth:login'
            'localisation_list',
            'identite_list',
        ]

    def location(self, url_name):
        return reverse(url_name)


sitemaps = {
    'roots': RootSitemap,
    'localisation': LocalisationSitemap,
    'identite': IdentiteSitemap,
}
