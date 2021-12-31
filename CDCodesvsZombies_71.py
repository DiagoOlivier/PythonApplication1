import sys
import math

# on fonce sur le premier sur le zombie 0
# score 28420
# 71 % de résultat


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
        if  i == 0:
            xnext = zombie_xnext
            ynext = zombie_ynext
    print(xnext, ynext )
