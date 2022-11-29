width = int(input())
length = int(input())
height = int(input())
box = input()

room_volume = width * length * height

while box != "Done":
    box = int(box)
    room_volume -= box
    if room_volume <= 0:
        print(f"No more free space! You need {abs(room_volume)} Cubic meters more.")
        break
    box = input()

if room_volume > 0:
    print(f"{room_volume} Cubic meters left.")
