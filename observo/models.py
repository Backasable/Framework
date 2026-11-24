from django.db import models

# Create your models here.
class Animal(models.Model):
    nom_commun = models.CharField(max_length=100)
    nom_savant = models.CharField(max_length=100)
    embranchement = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    ordre = models.CharField(max_length=100)
    sous_ordre = models.CharField(max_length=100)
    famille = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    IUCN = [
        ('EX','Éteint'),
        ('EW', 'Éteint à l\'état sauvage'),
        ('CR', 'En danger critique'),
        ('EN', 'En danger'),
        ('VU', 'Vulnérable'),
        ('NT', 'Quasi menacé'),
        ('LC', 'Préoccupation mineure'),
        ('DD', 'Données insuffisantes'),
        ('NE', 'Non évalué')
    ]
    status_iucn = models.CharField(max_length=2, choices=IUCN)
    description = models.TextField()

    def __str__(self):
        return self.nom_commun