# Solution pour Coding Game Chevaux de courses
liste =[]
n = int(input())
for i in range(n):
    r = int(input())
    liste.append(r)
liste.sort()
ecart = 100000000
if n == 2:
    ecart = liste[1]- liste[0]
else:
    for c in range(0,len(liste)-1):
        if liste[c+1] - liste[c] < ecart:
            ecart = liste[c+1] - liste[c] 
print(abs(ecart))
