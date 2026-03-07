def fun(liste=[]):
    resultaat =0
    for i in liste:
     resultat = resultat + i

    if resultaat <= 1:
        return str(resultat)+"ohm"
    else:
        return str( resultat)+"ohms"



liste = [1, 5, 6, 3]
print(fun(liste))