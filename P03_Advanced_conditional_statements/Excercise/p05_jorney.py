budget = float(input())
season = input()

spendings = 0
destination = ''
place = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == "summer":
        place = 'Camp'
        spendings = 0.30 * budget
    elif season == "winter":
        place = 'Hotel'
        spendings = 0.70 * budget
elif budget <= 1000:
    destination = 'Balkans'
    if season == "summer":
        place = 'Camp'
        spendings = 0.40 * budget
    elif season == "winter":
        place = 'Hotel'
        spendings = 0.80 * budget
elif budget > 1000:
    destination = 'Europe'
    place = 'Hotel'
    spendings = 0.90 * budget

print(f"Somewhere in {destination}")
print(f"{place} - {spendings:.2f}")
