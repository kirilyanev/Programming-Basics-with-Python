text = input()
character_sum = 0

a = 1
e = 2
i = 3
o = 4
u = 5

for ch in text:
    if ch == "a":
        character_sum += 1
    elif ch == "e":
        character_sum += 2
    elif ch == "i":
        character_sum += 3
    elif ch == "o":
        character_sum += 4
    elif ch == "u":
        character_sum += 5

print(character_sum)
