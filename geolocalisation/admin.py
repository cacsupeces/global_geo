from django.contrib import admin
from django.db.models import Count 
from django_markdown.admin import MarkdownModelAdmin
from .models import Identite, Localisation


@admin.register(Localisation)
class LocalisationAdmin(admin.ModelAdmin):
	list_display = ('cimetiere', 'position', 'identite_count')
	list_filter = ('cimetiere', )
	search_fields = ('cimetiere',)
	fieldsets = (
		('Informations Geolocalisation', {
			'fields': ('cimetiere', 'slug', 'position')
		}),
	)
	prepopulated_fields = {"slug": ('cimetiere',)}
	
	def get_queryset(self, request):
		queryset = super().get_queryset(request)
		return queryset.annotate(identite_number=Count('identite'))
	
	def identite_count(self, localisation):
		return localisation.identite_number
	
	identite_count.short_description = 'Nombre de Localisations'
	identite_count.admin_order_field = 'identite_number'





@admin.register(Identite)
class IdentiteAdmin(admin.ModelAdmin):
	list_display = ('nom', 'prenom')
	date_hierarchy = 'mort_le'
	list_filter = ('mort_le', )
	search_fields = ('nom', 'prenom')
	fieldsets = (
		('Identification', {
			'fields': ('nom', 'prenom', 'naissance', 'mort_le', 'code_certificat', 'pays', 'ville_village', 'mot_famille')
		}),
		('Chaque identité est liée à une localisation', {
			'fields': ('localisation',)
		}
		),
	)
	







