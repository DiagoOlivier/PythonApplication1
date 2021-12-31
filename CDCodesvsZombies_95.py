import sys
import math

# on fonce sur le dernier des humains de la liste
# score 30400
# 95 % de résultat


# game loop
while True:
    xnext = 0
    ynext = 0
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]

    print(human_x, human_y )