budget = int(input())
season = input()
fisherman_count = int(input())

ship_rent_price = 0
discount = 0
additioanal_discount = 0

if season == 'Spring':
    ship_rent_price = 3000
elif season == 'Summer' or season == 'Autumn':
    ship_rent_price = 4200
elif season == 'Winter':
    ship_rent_price = 2600

if fisherman_count <= 6:
    discount = ship_rent_price * 0.10
elif 7 <= fisherman_count <= 11:
    discount = ship_rent_price * 0.15
elif fisherman_count >= 12:
    discount = ship_rent_price * 0.25

if season == 'Spring' or season == 'Summer' or season == 'Winter':
    if fisherman_count % 2 == 0:
        additioanal_discount = 0.05

total_price = ship_rent_price - discount
total_price -= total_price * additioanal_discount

if budget >= total_price:
    print(f"Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")
