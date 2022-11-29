month = input()
accomodation = int(input())

price_for_studio = 0
price_for_apartment = 0
discount_studio = 0
discount_apartment = 0

if accomodation > 14:
    discount_apartment = 0.10

if month == "May" or month == "October":
    price_for_studio = 50
    if accomodation > 14:
        discount_studio = 0.30
    elif accomodation > 7:
        discount_studio = 0.05
    price_for_apartment = 65
elif month == "June" or month == "September":
    price_for_studio = 75.20
    if accomodation > 14:
        discount_studio = 0.20
    price_for_apartment = 68.70
elif month == "July" or month == "August":
    price_for_studio = 76
    price_for_apartment = 77

booking_price_studio = accomodation * price_for_studio
booking_price_apartment = accomodation * price_for_apartment

booking_price_studio -= discount_studio * booking_price_studio
booking_price_apartment -= discount_apartment * booking_price_apartment

print(f"Apartment: {booking_price_apartment:.2f} lv.")
print(f"Studio: {booking_price_studio:.2f} lv.")
