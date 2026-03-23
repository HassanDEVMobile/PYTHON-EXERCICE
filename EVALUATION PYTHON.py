def somme(liste=[]):
    somme = 0
    for i in range(0, len(liste)):
        somme = somme + liste[i]
    return somme


liste = []


def moyenne(somme, nombre):
    return somme / nombre


def mini(liste=[]):
    mini = list[0]
    for i in range(0, len(liste)):
        if liste[i] < mini:
            mini = liste[i]
    return mini


def maximum(liste=[]) :
    Maxi = liste[0]
    for i in range(0, len(liste)):
        if liste[i] > Maxi:
            Maxi = liste[i]
    return Maxi


nombre = int(input("Veuillez saisir le nombre de "
                   ""
                   "note que vous voulez saisir :"))
while nombre <= 0:
    print("Erreur de saisir le nombre de npote doit etre superieur a zero")
    nombre = int(input("Veuillez saisir le nombre de note que vous voulez saisir :"))
for i in range(nombre):
    i = int(input("Veuillez saisir la note:"))
    while i < 0:
        print("Le nombre saisir doit etre superieur ou egal a Zero")
        i = int(input("Veuillez saisir la note:"))
    liste.append(i)
print(str(somme(liste)))
print(str(moyenne(somme(liste),nombre)))
print(str(mini(liste)))
print(str(maximum(liste)))
