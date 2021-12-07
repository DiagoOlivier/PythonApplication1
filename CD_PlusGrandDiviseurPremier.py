import math
import time

def premiers(n):
    prem = list(range(2, n + 1))
    k = 2
    n_racine = math.sqrt(n)
    while k < n_racine:
        prem = [p for p in prem if p <= k or p % k != 0]
        k = prem[prem.index(k) + 1]  # nouveau nombre premier
    return prem


nombreaTester = 600851475143
Liste_premiers = premiers(int(math.sqrt(nombreaTester)))
print(Liste_premiers)
debut = time.time()
for i in reversed(Liste_premiers):
    if nombreaTester % i == 0:
        print(i)
        break


