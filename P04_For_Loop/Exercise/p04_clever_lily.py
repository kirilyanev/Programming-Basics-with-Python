age = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())
even = 0
odd = 0
money = 0
toys = 0

for even in range(2, age + 1):
    if even % 2 == 0:
        money += (even * 5) - 1

for odd in range(1, age + 1):
    if odd % 2 != 0:
        toys += 1

toy_price = single_toy_price * toys
money += toy_price

if money >= washing_machine_price:
    print(f"Yes! {money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money:.2f}")
