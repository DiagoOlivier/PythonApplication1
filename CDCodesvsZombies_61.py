
# si un seul humain, on fonce dessus
# sinon on fait la moyenne des zombies et on fonce dessus
# 61 % de résultat
xnext, ynet = 0,0

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
        if human_count == 1:
            xnext = human_x
            ynext = human_y
        elif  i == 0:
            xnext = zombie_xnext
            ynext = zombie_ynext
        else :
            xnext += zombie_xnext
            ynext += zombie_ynext
    if human_count != 1:
        xnext = int(xnext/zombie_count)
        ynext = int(ynext/zombie_count)
    print(xnext, ynext )