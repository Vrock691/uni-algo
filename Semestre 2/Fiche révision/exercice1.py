# Algorithme Calcul-Salaire

Cpt1 = 0
Cpt2 = 0
rep = 'O'

while rep == 'O' :
    Sal = float(input('Saisir le salaire : '))
    if Sal > 2000 :
        Cpt1 += 1
    if Sal < 1000 :
        Cpt2 += 1
    rep = input('Voulez vous saisir un autre salaire ? répondez par O/N').upper()

print('le nombre de salaires > 2000 est : ', Cpt1)
print('le nombre de salaires < 1000 est : ', Cpt2)