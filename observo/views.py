from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def about(request):
    return render(request, "observo/about.html")

def detail(request, pk):
    # Décodons le pk=pk 
    # le pk de gauche = le nom du champ sur lequel filtrer (la clé primaire)
    # le pk de droite = la valeur (le nombre capturé dans l'URL)

    object_animal = get_object_or_404(Animal, pk=pk)
    return render(request, "observo/detail.html", {"animal": object_animal})

def rep_tabulaire(request):
    animals = Animal.objects.all()
    return render(request, "observo/list_tab.html", {"animals": animals})

def new_animal(request):
    if request.method=="POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("animals")   
    else :
        form = AnimalForm()

    return render(request, "observo/new_animal.html", {"new_animal_form":form})

def delete_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        animal.delete()
        return redirect("animals")
    else :
        return render(request, "observo/delete_animal.html", {"animal_delete":animal})