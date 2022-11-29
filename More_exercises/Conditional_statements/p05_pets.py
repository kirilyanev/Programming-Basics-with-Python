import math

days = int(input())
left_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000

animals_food = ((dog_food + cat_food + turtle_food) * days)

if animals_food <= left_food:
    print(f"{math.floor(left_food - animals_food)} kilos of food left.")
else:
    print(f"{math.ceil(animals_food - left_food)} more kilos of food are needed.")
