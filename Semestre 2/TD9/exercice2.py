from modules import LireFichier

Chemin = str(input('Entrez le chemin du fichier : '))
Liste = LireFichier(Chemin)
print(Liste)

Somme = 0
for element in Liste :
    Somme += float(element)
Moyenne = Somme/len(Liste)
print(Moyenne)