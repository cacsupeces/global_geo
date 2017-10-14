# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields
import django_markdown.models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identite',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, verbose_name='Nom(s)')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom(s)')),
                ('naissance', models.DateField(verbose_name='Né(é) le')),
                ('mort_le', models.DateTimeField(verbose_name='Décédé(é) le')),
                ('code_certificat', models.CharField(verbose_name='Code du certificat de décès', max_length=100, unique=True)),
                ('pays', django_countries.fields.CountryField(max_length=2)),
                ('ville_village', models.CharField(max_length=100, verbose_name='Ville/Village')),
                ('mot_famille', django_markdown.models.MarkdownField(verbose_name='Mot de la famille')),
            ],
            options={
                'verbose_name': 'Identité',
                'verbose_name_plural': 'Identités',
            },
        ),
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cimetiere', models.CharField(max_length=100, verbose_name='Cimetière')),
                ('slug', models.SlugField(max_length=150)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
        migrations.AddField(
            model_name='identite',
            name='localisation',
            field=models.ForeignKey(to='geolocalisation.Localisation'),
        ),
    ]
