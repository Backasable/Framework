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

Question 2 :
Création de la template about, de la vue about 
ajout de 'observo.apps.ObservoConfig' dans INSTALLED_APPS 
Ajout du path dans cc2/urls.py et observo/urls.py pour que la template about puisse s'afficher