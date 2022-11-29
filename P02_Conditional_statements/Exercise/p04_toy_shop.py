price_excursion = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60 * puzzles
doll_price = 3 * dolls
bear_price = 4.10 * bears
minion_price = 8.20 * minions
truck_price = 2 * trucks

price = puzzle_price + doll_price + bear_price + minion_price + truck_price

toys = puzzles + dolls + bears + minions + trucks

if toys >= 50:
    price *= 0.75

earned_money = price * 0.9

if earned_money >= price_excursion:
    print(f"Yes! {earned_money - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - earned_money:.2f} lv needed.")
