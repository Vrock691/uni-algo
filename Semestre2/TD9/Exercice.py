# -*- coding: utf-8 -*-

# on importe les modules nécessaires
import os
import csv
os.chdir('/workspaces/uni-algo/Semestre2/TD9')

# on défini la variable globale
ListeGlobale = []

# on défini notre boucle infini tant que l'utilisateurs ne veut pas en sortir
x = 0
while x == 0:
    # on affiche le message d'acceuil
    print("0 - Fermer l'application\n 1 - Ajoutez un individu dans le liste \n 2 - afficher les individus de la liste \n 3 - Sauvegarder les individus dans un fichier \n 4 - Charger les individus à partir d'un fichier \n 5 - Vider la liste")  # Menu bastien

    # on cherche d'éventuelle erreur de saisie
    try:
        Reponse = int(input("Entrez le nombre choisi :"))
    except:
        print("seulement un nombre est attendu")

    # on définie chaque réponse dans un if

    if Reponse == 0:
        print("Vous avez choisi 0 -- Fin de l'application, merci de votre visite et à bientôt !")
        x = 1  # on met fin à la boucle -> fin de l'application

    if Reponse == 1:
        nom = str(input("Entrez votre nom :"))
        age = int(input("Quel est votre âge :"))
        taille = int(input("Quel est votre taille :"))
        # on ajoute le nouvel utilisateur à la variable globale
        ListeGlobale.append({"nom": nom, "age": age, "taille": taille})

    if Reponse == 2:
        print("Affichage de la liste des personnes :",
              ListeGlobale)  # Affichage de la liste globale

    if Reponse == 3:
        nom_fichier = str(input('entrez un nom de fichier'))
        fichier = open(nom_fichier, 'w')
        obj = csv.writer(fichier, delimiter=":")
        obj.writerow(ListeGlobale)
        fichier.close()

    if Reponse == 4:
        fichierPATH = input('Indiquer le nom du fichier à charger : ')
        fichierCSV = open(fichierPATH, 'r')
        liste = []
        source = csv.reader(fichierCSV, delimiter='', quotechar='')
        for ligne in source:
            liste.append(ligne)
        print('Fichier chargé !\n')
        fichierCSV.close()
        ListeGlobale = liste  # on écrase notre variable globale avec le contenu du csv

    if Reponse == 5:
        ListeGlobale.clear()  # On vide notre variable globale
        print('la liste a ete videe')
    if Reponse > 5:
        print("entrez un nombre en dessous de 5")
    if Reponse < 0:
        print("entrez un nombre au dessus de 0")
