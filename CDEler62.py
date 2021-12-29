# import numpy as np
# import itertools
# nombreCube3 = True
# a = 5026
# while nombreCube3 == True:
#     nombreCube = 0
#     print (a)
#     listPermutations = sorted(["".join(x) for x in itertools.permutations(str(a**3))])
#     for i in listPermutations:
#         if np.cbrt(int(i)).is_integer():
#             print(np.cbrt(int(i)))
#             nombreCube += 1
#     if nombreCube == 10:
#         nombreCube3 = False
#     else:
#         a += 1
#
# print(a**3)
# import time
# import time
#
# # time at the start of program
# start = time.time()
#
# # list to store cubes
# cubes = []
#
# # iterator
# i = 0
#
# # while loop
# while True:
#     # cube of the number
#     cube = sorted(list(str(i ** 3)))
#     # appending the cube to cubes list
#     cubes.append(cube)
#     # check if it occured 5 times
#     if cubes.count(cube) == 5:
#         # print the cube of the smallest such cube
#         print((cubes.index(cube)) ** 3)
#         break
#     i += 1
#
# # time at the end of program
# end = time.time()
#
# # total time taken
# print(end - start)


# Fonction qui range les chiffres d'un nombre dans l'ordre croissant.
def ordonner(n):
    return "".join(sorted([chiffre for chiffre in str(n)])) ### trouver la bonne fonction


# Fonction qui cherche la solution
def chercher():
    dic = {}
    n = 1
    while 1:
        cube_ordonné = ordonner(n**3)
        dic[cube_ordonné] = dic.setdefault(cube_ordonné, []) + [n]
        if len(dic[cube_ordonné]) == 3:
            return dic[cube_ordonné]
        n += 1


a = chercher()
b = [i ** 3 for i in a ]
print (a[0]**3)
print (a)
print (["".join(sorted(str(x))) for x in b ])

