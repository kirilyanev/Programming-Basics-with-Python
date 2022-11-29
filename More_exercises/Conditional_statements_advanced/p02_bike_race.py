juniors = int(input())
seniors = int(input())
trails = input()

tax_juniors = 0
tax_seniors = 0
discount = 0

if trails == "trail":
    tax_juniors = 5.50 * juniors
    tax_seniors = 7 * seniors
elif trails == "cross-country":
    tax_juniors = 8 * juniors
    tax_seniors = 9.50 * seniors
    if juniors + seniors >= 50:
        discount = 0.25 * (tax_juniors + tax_seniors)
elif trails == "downhill":
    tax_juniors = 12.25 * juniors
    tax_seniors = 13.75 * seniors
elif trails == "road":
    tax_juniors = 20 * juniors
    tax_seniors = 21.50 * seniors

money_collected = tax_juniors + tax_seniors - discount
money_collected -= 0.05 * money_collected

print(f"{money_collected:.2f}")