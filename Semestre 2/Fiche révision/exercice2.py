# Algorithme Blocage

CN = 0
CO = 0

for i in range(0, 600, 1) :
    Rep = input('Pour le blocage, répondez par OUI . Contre le blocage répondez par NON').upper()
    if Rep == 'OUI' :
        CO += 1
    elif Rep == 'NON' :
        CN += 1

print('Pour le blocage : ', CO)
print('Contre le blocage : ', CN)
