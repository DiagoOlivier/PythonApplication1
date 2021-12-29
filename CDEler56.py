sommeMax, aMax, bMax = 0, 0, 0
for a in range(2, 100):
    for b in range(2, 100):
        gogol = sum([int(i) for i in str(a ** b)])
        if gogol > sommeMax:
            sommeMax = gogol
            aMax = a
            bMax = b
print (sommeMax)

