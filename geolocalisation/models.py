from django.core.urlresolvers import reverse
from django.db import models
from geoposition.fields import GeopositionField
from django_markdown.models import MarkdownField
from django_countries.fields import CountryField


class LocalisationManager(models.Manager):
	
	def get_by_natural_key(self, pk):
		return self.get(pk=pk)



class Localisation(models.Model):
	cimetiere = models.CharField('Cimetière',max_length=100)
	slug = models.SlugField(max_length=150)
	position = GeopositionField()
	
	
	objects = LocalisationManager()
	
	def __str__(self):
		return self.cimetiere
	
	def get_absolute_url(self):
		return reverse('localisation_detail', kwargs={'pk':self.pk})
	
	def get_update_url(self):
		return reverse('localisation_update', kwargs={'pk': self.pk})
	
	def get_delete_url(self):
		return reverse('localisation_delete', kwargs={'pk': self.pk})
	
	def natural_key(self):
		return(self.pk,)
	
	permissions = (("view_future_localisation", "Can view unpublished Localisation"),)
	
	
	
	def get_feed_atom_url(self):
		return reverse('localisation_atom_feed', kwargs={'localisation_pk': self.pk})

	def get_feed_rss_url(self):
		return reverse('localisation_rss_feed',  kwargs={'localisation_pk': self.pk})
	
	
	
class IdentiteManager(models.Manager):
	
	def get_by_natural_key(self, pk):
		return self.get(pk=pk)
		

	
		
class Identite(models.Model):
	nom = models.CharField('Nom(s)', max_length=100)
	prenom = models.CharField('Prénom(s)',max_length=100)
	naissance = models.DateField('Né(é) le')
	mort_le = models.DateTimeField('Décédé(é) le')
	code_certificat = models.CharField('Code du certificat de décès', unique=True, max_length=100)
	pays = CountryField()
	ville_village = models.CharField('Ville/Village',max_length=100)
	mot_famille = MarkdownField('Mot de la famille')
	localisation = models.ForeignKey(Localisation)
	
	objects = IdentiteManager()
	
	def __str__(self):
		return self.nom
	
	
	def get_absolute_url(self):
		return reverse('identite_detail', kwargs={'pk': self.pk})
	
	def get_update_url(self):
		return reverse('identite_update', kwargs={'pk': self.pk})
	
	def get_delete_url(self):
		return reverse('identite_delete', kwargs={'pk': self.pk})
		
	
	def natural_key(self):
		return(self.pk)
	
	natural_key.dependencies = [
		'geolocalisation.localisation', 'user.user',
	]
	
	
	class Meta:
		verbose_name = "Identité"
		verbose_name_plural = "Identités"
	

	
	

	
	
	

	

