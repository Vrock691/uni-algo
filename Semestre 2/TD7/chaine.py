# fontions utiles

## Exercice 1

def Compter(mot, lettre):
    NombreLettre=0
    for caractere in mot:
        if caractere==lettre:
            NombreLettre+=1
    return NombreLettre

## Exercice 2

def Distincts(mot):
    dico={}
    NouveauMot=""
    for lettres in mot:
        if lettres not in dico:
            dico[lettres]=1
    for cles in dico:
        NouveauMot+=cles
    return NouveauMot

## Exercice 3

def frequences(mot):
    """
    Entrée : Un mot : str
    Sortie : Un dictionnaire avec le nombre d'occurences de chaque caractères
    Fonction : compte le nombre d'occurences de chaque lettres dans la phrase et la renvoie sous forme de dictionnaire
    """
    dico ={}
    for lettres in mot:
        if lettres not in dico:
            dico[lettres]=1
        else:
            dico[lettres]+=1
    return dico

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
