budget = float(input())
category = input()
fans = int(input())

tickets = 0

if fans <= 4:
    budget -= budget * 0.75
elif fans <= 9:
    budget -= budget * 0.60
elif fans <= 24:
    budget -= budget * 0.50
elif fans <= 49:
    budget -= budget * 0.40
elif fans >= 50:
    budget -= budget * 0.25

if category == "VIP":
    tickets = 499.99 * fans
elif category == "Normal":
    tickets = 249.99 * fans

if budget >= tickets:
    print(f"Yes! You have {budget - tickets:.2f} leva left.")
else:
    print(f"Not enough money! You need {tickets - budget:.2f} leva.")
