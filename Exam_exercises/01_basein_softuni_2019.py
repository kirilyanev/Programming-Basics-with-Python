import math
people = int(input())
entry_tax = float(input())
price_shezlong = float(input())
price_chadur = float(input())

chadyri_count = math.ceil(people / 2)
shezlong_count = math.ceil(0.75 * people)

suma = people * entry_tax + chadyri_count * price_chadur + shezlong_count * price_shezlong
final_suma = f"{suma:.2f}"

print(f"{final_suma} lv")
