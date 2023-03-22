from chaine import chiffre_cesar

mot=""
mot=input("entrez un mot ")
decalage=int(input("entrez le décalage :"))
mot.upper()
simple=chiffre_cesar(mot,decalage)
print(simple)