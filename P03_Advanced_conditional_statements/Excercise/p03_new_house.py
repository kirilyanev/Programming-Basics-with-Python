flower = input()
quantity = int(input())
budget = int(input())

flower_price = 0
discount_percentage = 0
higher_rate_percentage = 0

if flower == 'Roses':
    flower_price = 5
    if quantity > 80:
        discount_percentage = 0.10
elif flower == 'Dahlias':
    flower_price = 3.80
    if quantity > 90:
        discount_percentage = 0.15
elif flower == 'Tulips':
    flower_price = 2.80
    if quantity > 80:
        discount_percentage = 0.15
elif flower == 'Narcissus':
    flower_price = 3
    if quantity < 120:
        higher_rate_percentage = 0.15
elif flower == 'Gladiolus':
    flower_price = 2.50
    if quantity < 80:
        higher_rate_percentage = 0.20

total_price = flower_price * quantity

total_price -= total_price * discount_percentage
total_price += total_price * higher_rate_percentage

if budget >= total_price:
    print(f"Hey, you have a great garden with {quantity} {flower} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
