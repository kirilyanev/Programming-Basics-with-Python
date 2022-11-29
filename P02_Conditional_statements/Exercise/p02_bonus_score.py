number = int(input())
bonus = 0

if number > 1000:
    bonus = 0.10 * number
elif number > 100:
    bonus = 0.20 * number
elif number <= 100:
    bonus = 5

if number % 2 == 0:
    bonus += 1
if number % 5 == 0 and number % 2 != 0:
    bonus += 2

print(bonus)
print(number + bonus)
