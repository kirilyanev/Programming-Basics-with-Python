days_of_vacation = int(input())
room_type = input()
rating = input()

room_for_one_person = 18 * (days_of_vacation - 1)
apartment = 25 * (days_of_vacation - 1)
president_apartment = 35 * (days_of_vacation - 1)

if room_type == "apartment":
    if days_of_vacation < 10:
        apartment -= apartment * 0.30
    elif 10 <= days_of_vacation <= 15:
        apartment -= apartment * 0.35
    elif days_of_vacation > 15:
        apartment -= apartment * 0.50
elif room_type == "president apartment":
    if days_of_vacation < 10:
        president_apartment -= president_apartment * 0.10
    elif 10 <= days_of_vacation <= 15:
        president_apartment -= president_apartment * 0.15
    elif days_of_vacation > 15:
        president_apartment -= president_apartment * 0.20

if rating == "positive":
    room_for_one_person += room_for_one_person * 0.25
    apartment += apartment * 0.25
    president_apartment += president_apartment * 0.25
elif rating == "negative":
    room_for_one_person -= room_for_one_person * 0.10
    apartment -= apartment * 0.10
    president_apartment -= president_apartment * 0.10

if room_type == "room for one person":
    print(f"{room_for_one_person:.2f}")
elif room_type == "apartment":
    print(f"{apartment:.2f}")
elif room_type == "president apartment":
    print(f"{president_apartment:.2f}")
