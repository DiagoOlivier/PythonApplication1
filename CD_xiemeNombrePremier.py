import math


def is_prime(nb):
    if nb == 1:
        return False
    if nb == 2:
        return True
    elif nb % 2 == 0:
        return False
    for i in range(3, int(nb ** 0.5) + 1, 2):
        if nb % i == 0:
            return False
    return True


premier = [1, 2, 3]
i = 5
for i in range (7,1000000,2):
    if is_prime(i):
        premier.append(i)
        if len (premier) == 100001:
            break
print(len(premier))
print(max(premier))
