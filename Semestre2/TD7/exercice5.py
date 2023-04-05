from chaine import annagrammes

mot_1=str(input("entrez un mot "))
mot_2=str(input("entrez un mot "))
mot_1=mot_1.upper()
mot_2=mot_2.upper()
simple=annagrammes(mot_1,mot_2)
print(simple)