from modules import SauvegardeListeFichier
from modules import SaisieListe


nombreElements = int(input("Entrez le nombre d'éléments de la liste"))
Liste = SaisieListe(nombreElements)

Chemin = str(input("Entrez le chemin d'accès du fichier : "))
SauvegardeListeFichier(Liste, Chemin)
