money = float(input())

coin_counter = 0

while money > 0:
    if money >= 2.00:
        money -= 2.00
        money = round(money, 2)
        coin_counter += 1
    elif 1.00 <= money <= 2.00:
        money -= 1.00
        money = round(money, 2)
        coin_counter += 1
    elif 0.50 <= money < 1:
        money -= 0.50
        money = round(money, 2)
        coin_counter += 1
    elif 0.20 <= money < 0.50:
        money -= 0.20
        money = round(money, 2)
        coin_counter += 1
    elif 0.10 <= money < 0.20:
        money -= 0.10
        money = round(money, 2)
        coin_counter += 1
    elif 0.05 <= money < 0.10:
        money -= 0.05
        money = round(money, 2)
        coin_counter += 1
    elif 0.02 <= money < 0.05:
        money -= 0.02
        money = round(money, 2)
        coin_counter += 1
    elif 0.01 <= money < 0.02:
        money -= 0.01
        money = round(money, 2)
        coin_counter += 1

print(coin_counter)
