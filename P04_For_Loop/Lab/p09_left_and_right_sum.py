integers = int(input())
number = 0
sum_left = 0
sum_right = 0

for i in range(1, integers * 2 + 1):
    number = int(input())
    if i <= integers:
        sum_left += number
    else:
        sum_right += number

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {abs(sum_left - sum_right)}")
