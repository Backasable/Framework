from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.
def about(request):
    return render(request, "observo/about.html")

def detail(request, pk):
    # Décodons le pk=pk 
    # le pk de gauche = le nom du champ sur lequel filtrer (la clé primaire)
    # le pk de droite = la valeur (le nombre capturé dans l'URL)

    object_animal = get_object_or_404(Animal, pk=pk)
    return render(request, "observo/detail.html", {"animal": object_animal})