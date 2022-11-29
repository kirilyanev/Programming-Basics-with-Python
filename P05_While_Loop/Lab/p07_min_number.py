import sys

user_input = input()
min_number = sys.maxsize

while user_input != "Stop":
    user_input = int(user_input)
    if user_input < min_number:
        min_number = user_input

    user_input = input()

print(min_number)
