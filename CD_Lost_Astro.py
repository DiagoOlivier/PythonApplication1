n = int(input())
resultat= ""

#Excercice CodinGame Lost Astronaute
message = input().replace("  "," ").split(" ")

for m in message:
    if len(m) == 7: # Code binaire
        resultat += chr(int(m, 2)) 
    elif m == '40' or m == '100000' or m == ""  :
         resultat += " " # cas de l'espace en octal et hexadecimal et en UTF 8
    elif len(m) == 3: # #Octal --> UTF 
        resultat += chr(int(m, 8))
    elif len(m) == 2: # hexadecimal --> UTF
        resultat += chr(int(m, 16))
    else:
       resultat += m
print(resultat)