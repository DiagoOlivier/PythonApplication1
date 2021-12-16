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


premier = [ 2, 3]
i = 5
somme = 5
while i < 2000000:
    if is_prime(i):
        somme += i
    i += 2

print (somme)
