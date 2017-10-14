from django.contrib.sitemaps import (GenericSitemap, Sitemap)

from .models import Localisation, Identite

identite_sitemap_dict = {
    'queryset': Identite.objects.all(),
}


IdentiteSitemap = GenericSitemap(identite_sitemap_dict)


class LocalisationSitemap(Sitemap):

    def items(self):
        return Localisation.objects.all()

    def lastmod(self, startup):
        if localisation.identite_set.exists():
            return (localisation.identite_set.latest().mort_le)
        else:
            return localisation.mort_le
