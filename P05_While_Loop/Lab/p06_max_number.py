import sys

user_input = input()
max_number = -sys.maxsize

while user_input != "Stop":
    user_input = int(user_input)
    if user_input > max_number:
        max_number = user_input

    user_input = input()

print(max_number)
