# Algorithme Étudiant licence

TabNotes = []

nb = int(input("Saisir le nombre d'étudiant : "))

# Saisie des notes
for i in range(1, nb+1, 1) :
    TabNotes.append(float(input("Entrez la note de l'étudiant N°"+str(i)+' : ')))

# Affichage de la note de l'étudiant N°3
print(TabNotes[2]) # index 0 étant l'étudiant 1, l'étudiant 3 est à l'index 2

# Affichage de la note d'un étudiant donné
Num =  int(input("Donnez le numéro de l'étudiant : ")) - 1 # soustraction pour l'index encore une fois
print("La note de l'étudiant N°"+str(int(Num+1))+' est '+str(TabNotes[Num]))

# Affichage des 5 meilleures notes
TabNotesTrié = TabNotes
TabNotesTrié.sort(reverse=True)
for i in range(0, 5, 1) :
    print('La note n°'+str(i+1)+' du classement est '+str(TabNotesTrié[i]))

# Affichage de la moyenne
Somme = 0
Moyenne = 0
for i in range(0, nb) :
    Somme = Somme + TabNotes[i]
Moyenne = Somme / nb
print('La moyenne du groupe est ', Moyenne)

# Affichage de la note maximale avec le numéro de l'étudiant
Max = 0
for i in range(0, nb, 1) :
    if TabNotes[i] > Max :
        Max=TabNotes[i]
        K = i
print('La plus haute note est : ' ,Max, 'de l’étudiant N°', K+1)
