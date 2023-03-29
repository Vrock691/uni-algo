from modules import SaisieListe, CalculVecteurCroisé, SauvergarderListes

nombreElements = int(input('Entrez la longueur des listes : '))
ListeX = SaisieListe(nombreElements)
ListeY = SaisieListe(nombreElements)
print(str(CalculVecteurCroisé(ListeX, ListeY)))
Chemin = input('entrez le chemin du fichier : ')
SauvergarderListes(ListeX, ListeY, Chemin)
