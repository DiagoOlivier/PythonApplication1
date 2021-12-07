import math

w = 1
h = 80
x0 = 1
y0 = 1
x = 1
y = 4
y_max = h
x_max = w
y_min = 0
x_min = 0
RE = True
bomb_dir = ""
while RE:
    bomb_dir = input()
    if bomb_dir == "U":
        y_min = y0
        y0 = math.floor(y0 -((y0 - y_min)/2))

    elif bomb_dir == "UR":
        y0 = int(y0 - y0 / 2)
        x0 = int(x0 + (w - x0) / 2)
    elif bomb_dir == "R":
        x0 = int(x0 + (w - x0) / 2)
    elif bomb_dir == "DR":
        x0 = int(x0 + (w - x0) / 2)
        y0 = int(y0 + (h - y0) / 2)
    elif bomb_dir == "D":
        y_max = y0
        y0 = math.ceil(y0 + ((y_max - y0)/2))
    elif bomb_dir == "DL":
        y0 = int(y0 + (h - y0) / 2)
        x0 = int(x0 - x0 / 2)
    elif bomb_dir == "L":
        x0 = int(x0 - x0 / 2)
    elif bomb_dir == "UL":
        x0 = int(x0 - x0 / 2)
        y0 = int(y0 - y0 / 2)
    # DEBUG
    if x == x0 and y == y0:
        RE = False
    # End DEBUG
    print(x0, y0)