light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
while True:
    remaining_turns = int(input())
    if light_x == initial_tx and light_y < initial_ty:
        print("N")
        initial_ty -= 1
    if light_x == initial_tx and light_y > initial_ty:
        print("S")
        initial_ty += 1
    elif light_x > initial_tx and light_y < initial_ty:
        print("NE")
        initial_ty -= 1
        initial_tx += 1
    elif light_x < initial_tx and light_y < initial_ty:
        print("NO")
        initial_ty -= 1
        initial_tx -= 1
    elif light_x < initial_tx and light_y == initial_ty:
        print("O")
        initial_tx -= 1
    elif light_x > initial_tx and light_y == initial_ty:
        print("E")
        initial_tx += 1
    if light_x > initial_tx and light_y > initial_ty:
        print("SE")
        initial_ty += 1
        initial_tx -= 1
    if light_x < initial_tx and light_y < initial_ty:
        print("SO")
        initial_ty -= 1
        initial_tx -= 1
    # A single line providing the move to be made: N NE E SE S SW W or NW
