import sys
import math

# On fonce sur le premier des humains
# 20830 points
# 100% de résultats


# game loop
while True:
    xnext = 0
    ynext = 0
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        if i == 0:
            xnext = human_x
            ynext = human_y
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]

    print(xnext, ynext )
