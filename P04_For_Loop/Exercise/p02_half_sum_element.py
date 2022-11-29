import sys

integers = int(input())
biggest_num = -sys.maxsize
numbers_sum = 0
number = 0

for num in range(1, integers + 1):
    number = int(input())
    numbers_sum += number
    if number > biggest_num:
        biggest_num = number
numbers_sum -= biggest_num

if biggest_num == numbers_sum:
    print("Yes")
    print(f"Sum = {biggest_num}")
else:
    print("No")
    print(f"Diff = {abs(numbers_sum - biggest_num)}")
