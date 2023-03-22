# fontions utiles

## Exercice 1

def Compter(mot, lettre):
    NombreLettre=0
    for caractere in mot:
        if caractere==lettre:
            NombreLettre+=1
    return NombreLettre

## Exercice 2

def dinstincts(mot):
    lettre=mot
    lettre_unique = []
    lettre_fini=""
    [lettre_unique.append(lettre) for lettre in lettre if lettre not in lettre_unique]
    for i in range(0,len(lettre_unique)):
        lettre_fini+=lettre_unique[i]
    return(lettre_fini)

## Exercice 3


# Exercice 4


def inclusion(mot_1, mot_2) :
    mot_1=mot_1.upper()
    mot_2=mot_2.upper()
    if mot_1 in mot_2:
        return True
    else:
        return False

# Exercice 5

def annagrammes(mot_1,mot_2):
    anagrammes = 0
    if len(mot_1)!=len(mot_2):
        rep = False
    else:
        for lettres1 in mot_1:
            for lettres2 in mot_2:
                if lettres1 == lettres2:
                    anagrammes +=1
        if anagrammes == len(mot_2):
            rep = True
    return rep


#Exercice 6

def chiffre_cesar(mot,decalage):
    """
    Rajouter dans le module « » la fonction chiffre_cesar(mot,decalage), laquelle renvoie une chaîne de caractères
    - mot représente une chaîne de caractères
    - décalage est un entier que l’on considère positif
    - La fonction renvoie l’équivalent après cryptage du mot
    - L’algorithme de cryptographie consiste à remplacer chaque lettre d’un mot par une autre lettre en
    opérant un décalage dans l’alphabet. On considère que toutes les lettres sont en majuscule (26 lettres
    en tout, de ‘A’ à ‘Z’). Par exemple, « TOTO » avec un décalage de 2, deviendrait « VQVQ ».
    - Attention, si le décalage nous fait déborder de ‘Z’, on recommence au début de l’alphabet. Par
    exemple, « ZAZA » avec un décalage de 3 devient « CDCD ».
    Remarque : (1) Une piste possible consiste à former une chaîne de référence avec toutes les lettres de
    l’alphabet (« ABCDEFGHIJKLMNOPQRSTUVWXYZ »), vous pourrez ainsi y trouver la lettre à
    coder et la valeur de substitution après décalage. (2) find() permet de trouver la position d’une
    lettre dans un mot (ex. « carte ».find(« a ») renvoie 1 [puisque les indices commencent à 0]).
    Dans votre programme principal (exercice6.py), vous devez :
     Importer le module
     Effectuer la saisie du mot et le convertir en majuscule
     Effectuer la saisie du décalage
     Faire appel à la fonction pour produire le mot crypté
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mot = mot.upper()
    nouveauMot=""
    for lettres in mot:
        for indice in range(len(alphabet)):
            if lettres==alphabet[indice] and indice <= 26-decalage:
                indiceLettres = indice + decalage
                nouveauMot+= alphabet[indiceLettres]
            elif lettres==alphabet[indice] and indice > 26-decalage :
                Nouveaudecalage = indice + decalage - 26
                indiceLettres = Nouveaudecalage
                nouveauMot+=alphabet[indiceLettres]
    return nouveauMot
