from django.core.paginator import (EmptyPage, PageNotAnInteger, Paginator)
from django.views.generic import (View, CreateView, DeleteView, DetailView, ListView)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import (UserRegistrationForm, LocalisationForm, IdentiteForm)
from .models import Localisation, Identite
from core.utils import UpdateView
from .utils import (IdentiteGetObjectMixin, PageLinksMixin, LocalisationContextMixin)
from django.core.urlresolvers import reverse_lazy
from user.decorators import require_authenticated_permission





@require_authenticated_permission('geolocalisation.add_localisation')
class LocalisationCreate(CreateView):
	form_class = LocalisationForm
	model = Localisation
	
@require_authenticated_permission('geolocalisation.change_localisation')
class LocalisationUpdate(UpdateView):
	form_class = LocalisationForm
	model = Localisation
	
@require_authenticated_permission('geolocalisation.delete_localisation')
class LocalisationDelete(DeleteView):
	model = Localisation
	success_url = reverse_lazy('localisation_list')
	
class LocalisationDetail(DetailView):
	queryset = (Localisation.objects.prefetch_related('identite_set'))	
		

class LocalisationList(PageLinksMixin, ListView):
	paginate_by = 5
	model = Localisation	

@require_authenticated_permission('geolocalisation.add_identite')
class IdentiteCreate(CreateView):
	form_class = IdentiteForm
	model = Identite
	
@require_authenticated_permission('geolocalisation.change_identite')
class IdentiteUpdate(UpdateView):
	form_class = IdentiteForm
	model = Identite
	
@require_authenticated_permission('geolocalisation.delete_identite')	
class IdentiteDelete(DeleteView):
	model = Identite
	success_url = reverse_lazy('identite_list')
	
class IdentiteDetail(DetailView):
	queryset = (Identite.objects.all().prefetch_related('localisation'))	
	
class IdentiteList(PageLinksMixin, ListView):
	paginate_by = 5
	model = Identite
	

		
