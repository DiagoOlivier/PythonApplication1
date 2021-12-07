import random, time
tour = int(input("Combien d'itérations ?\n"))
compteur = 0
debut = time.time()
for i in range(tour):
    if random.random()**2 + random.random()**2 < 1: compteur += 1
fin = time.time()
print (f' Pour {tour} itérations pi vaut {4*compteur/tour}')
print(f'en {round(fin - debut,3)} secondes')