from django.core.management.base import (BaseCommand, CommandError)
from django.utils.text import slugify

from ...models import Localisation


class Command(BaseCommand):
    help = 'Create new Localisation.'

    def add_arguments(self, parser):
        parser.add_argument(
            'localisation_cimetiere',
            default=None,
            help='New localisation name.')

    def handle(self, **options):
        localisation_cimetiere = options.pop('localisation_cimetiere', None)
        Localisation.objects.create(cimetiere=localisation_cimetiere, slug=slugify(localisation_cimetiere))
