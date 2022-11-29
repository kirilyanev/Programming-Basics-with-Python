import math

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
present_price = float(input())

total_sum = magnolia_count * 3.25 + hyacinth_count * 4 + rose_count * 3.50 + cactus_count * 8
total_sum -= total_sum * 0.05

if total_sum >= present_price:
    print(f"She is left with {math.floor(total_sum - present_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(present_price - total_sum)} leva.")
