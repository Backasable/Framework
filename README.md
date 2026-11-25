# Framework projet CC blanc
Membre du groupe : 
Xenos 

Question 1 : 
## Modélisation des observations
Observation contiendra les attributs : 
- Dateheure, type : DateTimeField

GPS : indique les coordonnées GPS de l'observation
- longitude, type : FloatField
- latitude, type : FloatField

- Animal : reférence de l'animal observé, type : ForeignKey
- Description : décrit l'observation, type : TextField

## Commandes utilisées : 
```bash
USERNAME=$(whoami) USERID=$(id -u) docker-compose up -d --build
docker exec -ti fw1-tp2-ubuntu bash
django-admin startproject cc2 .
python manage.py startapp observo
python manage.py runserver 0.0.0.0:8000
```

## Question 3 : 
Création du compte admin 

## Commandes utilisées : 
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Question 4 : 
Création du modèle Animal 

## Commandes utilisées : 
```bash
python manage.py makemigrations
python manage.py migrate
```

## Question 5 : 

Ajout de la fixture animals.json 
avec les 10 animaux

## Commandes utilisées
```bash
python manage.py loaddata animals
```

## Question 6 : 
Ajout de la template Detail 
et de son chemin dans urls.py 

## Question 7 : 
Ajout de la template liste_tab et de la vue rep_tabulaire pour lister de manière tabulaire tout les animaux avec leur lien 

## Question 8 : 
Ajout du formulaire AnimalForm de sa template associé : new_animal.html et de 
son chemin dans observo/urls.py

# Question 9 :
Ajout de l'option de suppression avec sa template en plus de son chemin dans urls.py



