from django.contrib import admin
from django.urls import path, include

# Note : 
"""
l'urls.py du projet ici cc2
est la première chose que va voir django
les requête serveur pour consulter tel page seront 
transmise à l'app observo à partir d'ici
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    # la fct include() est ce qui permet de transmettre à l'app observo les requêtes serveurs
    path('', include('observo.urls'))
]
