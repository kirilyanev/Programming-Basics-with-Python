integers = int(input())
number = 0
r_one = 0
r_two = 0
r_three = 0
r_four = 0
r_five = 0

for num in range(1, integers + 1):
    number = int(input())
    if number < 200:
        r_one += 1
    elif number < 400:
        r_two += 1
    elif number < 600:
        r_three += 1
    elif number < 800:
        r_four += 1
    else:
        r_five += 1

print(f"{r_one / integers * 100:.2f}%")
print(f"{r_two / integers * 100:.2f}%")
print(f"{r_three / integers * 100:.2f}%")
print(f"{r_four / integers * 100:.2f}%")
print(f"{r_five / integers * 100:.2f}%")
