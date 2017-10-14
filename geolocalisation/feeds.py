from datetime import datetime

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import (Atom1Feed, Rss201rev2Feed)

from .models import Localisation


class BaseLocalisationFeedMixin():

    def description(self, localisation):
        return "News related to {}".format(localisation.cimetiere)

    def get_object(self, request, localisation_pk):
        # equivalent to GCBV get() method
        return get_object_or_404(Localisation, pk__iexact=localisation_pk)

    def items(self, localisation):
        return localisation.identite_set.all()[:10]

    

    def item_title(self, identite):
        return identite.nom

    def link(self, localisation):
        return localisation.get_absolute_url()

    

    def title(self, localisation):
        return localisation.cimetiere


class AtomLocalisationFeed(BaseLocalisationFeedMixin, Feed):
    feed_type = Atom1Feed


class Rss2LocalisationFeed(BaseLocalisationFeedMixin, Feed):
    feed_type = Rss201rev2Feed
