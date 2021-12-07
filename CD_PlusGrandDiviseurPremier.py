import math
import time

def premiers(n):
    prem = list(range(2, n + 1))
    k = 2
    nRacine = math.sqrt(n)
    while k < nRacine:
        prem = [p for p in prem if p <= k or p % k != 0]
        k = prem[prem.index(k) + 1]  # nouveau nombre premier
    return prem


nombreATester = 600851475143
Liste_premiers = premiers(int(math.sqrt(nombreATester)))
print(Liste_premiers)
debut = time.time()
for i in reversed(Liste_premiers):
    if nombreATester % i == 0:
        print(i)
        break


