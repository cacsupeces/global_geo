import subprocess

nom = "export DJANGO_SETTINGS_MODULE=global_geo.settings.dev"
chemin = "/home/ali/webApps/GEOLOCALISER/global_geo/"


subprocess.call([nom, chemin])


