people_count = int(input())
season = input()

price_for_person = 0

if people_count <= 5:
    if season == "spring":
        price_for_person = 50.00
    elif season == "summer":
        price_for_person = 48.50
    elif season == "autumn":
        price_for_person = 60.00
    elif season == "winter":
        price_for_person = 86.00
elif people_count > 5:
    if season == "spring":
        price_for_person = 48.00
    elif season == "summer":
        price_for_person = 45.00
    elif season == "autumn":
        price_for_person = 49.50
    elif season == "winter":
        price_for_person = 85.00

vacation_price = price_for_person * people_count

if season == "summer":
    print(f"{vacation_price - (vacation_price * 0.15):.2f} leva.")
elif season == "winter":
    print(f"{vacation_price + (vacation_price * 0.08):.2f} leva.")
else:
    print(f"{vacation_price:.2f} leva.")