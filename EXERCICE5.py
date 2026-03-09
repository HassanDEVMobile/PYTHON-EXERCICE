def fun(liste=[]):
    resultat = 0
    for i in range(0,len(liste)):
     resultat = resultat +liste[i]

    if resultat <= 1:
        return str(resultat)+" ohm"
    else:
        return str( resultat)+" ohms"




print(fun( [1, 5, 6, 3]))
print(fun([16, 3.5, 6]))
print(fun([0.5, 0.5]))