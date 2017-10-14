# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.hashers import  make_password
from django.db import models, migrations


def add_user_data(apps, schema_editor):
	Group = apps.get_model('auth', 'Group')
	Permission = apps.get_model('auth', 'Permission')
	Profile = apps.get_model('user', 'Profile')
	User = apps.get_model('user', 'User')
	ali = User.objects.create(email='ibrahimgeyd@gmail.com',password=make_password('eces2017'), is_active=True, is_staff=True, is_superuser=True)
    
    
	
	



class Migration(migrations.Migration):

    dependencies = [
		('geolocalisation', '0002_localisation_permissions'),
		('geolocalisation', '0003_identite_permissions'),
        ('user', '0001_initial'),
    ]

    operations = [
		 migrations.RunPython(add_user_data, )
    ]
