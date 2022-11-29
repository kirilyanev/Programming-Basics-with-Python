import math

days_away = int(input())
food_kg = int(input())
first_food_for_day = float(input())
second_food_for_day = float(input())
third_food_for_day = float(input())

needed_food = first_food_for_day * days_away + second_food_for_day * days_away + \
              third_food_for_day * days_away

if needed_food <= food_kg:
    print(f"{math.floor(food_kg - needed_food)} kilos of food left.")
else:
    print(f"{math.ceil(needed_food - food_kg)} more kilos of food are needed.")