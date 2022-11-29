cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_width * cake_length

pieces = input()

while pieces != "STOP":
    pieces = int(pieces)
    cake_pieces -= pieces
    if cake_pieces <= 0:
        print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
        break
    pieces = input()

if cake_pieces > 0:
    print(f"{cake_pieces} pieces are left.")
