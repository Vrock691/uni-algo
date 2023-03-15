# Algorithme Stock 

Mstock = []

for i in range(0, 200, 1) :
    Mstock.append(int(input('Saisir la quantité du produit N°'+str(i)+': ')))

for i in range(0, 200, 1) :
    if Mstock[i] < 15 :
        print('Le produit N°',i, 'est en stock minimum, sa quantité est ',Mstock[i])
