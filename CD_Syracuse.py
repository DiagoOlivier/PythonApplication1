longueurMax = 0
nombreMax = 0
for i in range(2,10000000):
    compteur = 0
    initial = i
    while i != 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = 3 * i + 1
        compteur += 1
    if compteur + 1 > longueurMax:
        longueurMax = compteur + 1
        nombreMax = initial
        print(nombreMax,longueurMax)
print(nombreMax,longueurMax )

