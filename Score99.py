from itertools import combinations
import math
nombres =[]
index = 1
possibilite = {}
addition ={}
#Question 1 
reponse = input ("Quels sont les nombres possibles ? \n")
nombres = reponse.split()
combinaisons = combinations(nombres,3)
# creation d'un dictionnaire des combinaisons
for combinaison in combinaisons:
    possibilite [index] = combinaison
    index += 1
# creation d'un dictionnaire des additions
for index,nombres in possibilite.items():
   addition [index] = sum (int(nombres))
# questions 
while reponse != 0:
    reponse = int(input("Quel nombre est présent"))
    for key,mult in addition.items():
        if mult == 99 - reponse:
            print(possibilite[key])



