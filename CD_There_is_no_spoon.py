
quadrillage =[]

width = 3 #int(input())  # the number of cells on the X axis
height = 3  #int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    quadrillage.append(line)
for i in range(height):
    for j in range(width):
        temp = True
        if quadrillage[i][j] == "0":
            re = str(j) + " " + str(i) + " "
            if j != width-1: # and ("0" in quadrillage[i]): # recherche d'un 0 à droite
                for k in range(j+1, width):
                    if quadrillage[i][k] == "0":
                        re += str(k) + " " + str(i) + " "
                        temp = False
                        break
                if temp:
                    re += "-1 -1 "
            else:
                re += "-1 -1 "
            if i != height-1: # recherche d'un 0 en bas
                temp = True
                for k in range(i+1, height):
                    if quadrillage[k][j] == "0":
                        re += str(j) + " " + str(k)
                        temp = False
                        break
                if temp:
                    re += "-1 -1"
            else:
                re += "-1 -1"
            print(re)