import os
os.chdir('/workspaces/uni-algo/Semestre 2/TD9')


def SaisieListe(nombreElements):
    listeFinale = []
    for i in range(0, nombreElements):
        valeur = int(input('Entrez une valeur entière : '))
        listeFinale.append(valeur)
    return listeFinale


def SauvegardeListeFichier(Liste, Chemin):
    Fichier = open(Chemin+'.txt', 'a')
    for element in Liste:
        Fichier.write("\n" + str(element))
    Fichier.close()


def LireFichier(Chemin):
    Fichier = open(Chemin+'.txt', 'r')
    Liste = Fichier.readlines()
    Fichier.close()
    return Liste


def CalculVecteurCroisé(ListeX, ListeY):
    résultatSomme = 0
    for i in range(0, len(ListeX) - 1):
        résultatSomme += (float(ListeX[i])*float(ListeY[i]))
    return résultatSomme


def SauvergarderListes(ListeX, ListeY, Chemin):
    Fichier = open(Chemin+'.txt', 'a')
    for i in range(0, len(ListeX) - 1):
        Fichier.write(str(ListeX[i])+';'+str(ListeY[i]))
    Fichier.close()


def chargerListes(Chemin):
    ListeX = []
    ListeY = []
    Fichier = open(Chemin+'.txt', 'r')
    Lignes = Fichier.readlines()
    for Ligne in Lignes:
        Splitted = Ligne.split(';')
        ListeX.append(Splitted[0])
        ListeY.append(Splitted[1])
    return [ListeX, ListeY]