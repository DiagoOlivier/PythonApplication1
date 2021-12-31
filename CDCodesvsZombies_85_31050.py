import sys
import math

# on fonce sur le dernier des humains de la liste en retirant 990 a ses coordonnées
# si il reste qu'un humain on fonce sur la moyennes des coordonnées des zombies
# 95 % de résultat


# game loop
while True:
    xnext = 0
    ynext = 0
    xzombiemoyen = 0
    yzombiemoyen = 0
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        xzombiemoyen += zombie_xnext
        yzombiemoyen += zombie_ynext
    xzombiemoyen = int(xzombiemoyen/zombie_count)
    yzombiemoyen = int( yzombiemoyen/zombie_count)
    if human_count == 1:
        xnext = xzombiemoyen
        ynext = yzombiemoyen
    else:
        if human_x - 990 <= 0:
            xnext = 0
            ynext = human_y - 990
        elif human_y -990 <= 0:
            xnext = human_x - 990
            ynext = 0
        else:
            xnext = human_x - 990
            ynext = human_y - 990

    print(xnext, ynext )