needed_money = float(input())
available_money = float(input())

day_spend = 0
day_saved = 0
days = 0

while available_money < needed_money:
    action_taken = input()
    money = float(input())
    days += 1
    if action_taken == 'spend':
        day_spend += 1
        day_saved = 0
        if available_money <= money:
            available_money = 0
        else:
            available_money -= money
    elif action_taken == 'save':
        day_spend = 0
        day_saved += 1
        available_money += money
    if day_spend >= 5:
        print("You can't save the money.")
        print(days)
        break

if available_money >= needed_money:
    print(f"You saved the money for {days} days.")
