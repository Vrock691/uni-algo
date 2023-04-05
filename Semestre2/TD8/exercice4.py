from modules import CalculVecteurCroisé, chargerListes

Chemin = input('Entrez le nom du fichier : ')
ListeFusionnées = chargerListes(Chemin)

ListeX = ListeFusionnées[0]
ListeY = ListeFusionnées[1]
print(ListeX)
print(ListeY)
print(CalculVecteurCroisé(ListeX, ListeY))
