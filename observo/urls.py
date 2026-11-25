from django.urls import path
from .views import *

urlpatterns = [
# Chaque route suit le schéma :
#   path("chemin/", vue, name="nom")
#     • "chemin/" : l'URL à reconnaître (relative au préfixe où l'app est incluse)
#     • vue       : la fonction de views.py appelée quand l'URL correspond
#     • name="…"  : nom interne pour désigner cette URL sans la réécrire en dur
#                   (ex. dans un template : {% url 'about' %})
    path('about/', about, name="about"),
    path('animals/<int:pk>', detail, name='detail_animals'),
    path('animals', rep_tabulaire, name='animals'),
    path('new_animal', new_animal, name='new_animal'),
]