budget = float(input())
actors = int(input())
cloth_price = float(input())

decor = budget * 0.1
total_clothing_price = actors * cloth_price

if actors > 150:
    total_clothing_price *= 0.9

expenses = decor + total_clothing_price

if expenses <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - expenses:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {expenses - budget:.2f} leva more.")
