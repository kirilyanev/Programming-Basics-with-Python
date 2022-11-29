number_one = int(input())
number_two = int(input())
user_operator = input()

result = 0
odd_or_even = ''

if user_operator == "+":
    result = number_one + number_two
elif user_operator == "-":
    result = number_one - number_two
elif user_operator == "*":
    result = number_one * number_two
elif user_operator == "/":
    if number_one != 0 and number_two != 0:
        result = number_one / number_two
    else:
        print(f"Cannot divide {number_one} by zero")
elif user_operator == "%":
    if number_one != 0 and number_two != 0:
        result = number_one % number_two
    else:
        print(f"Cannot divide {number_one} by zero")


if result % 2 == 0:
    odd_or_even = 'even'
else:
    odd_or_even = 'odd'

if user_operator == '+' or user_operator == '-' or user_operator == '*':
    print(f"{number_one} {user_operator} {number_two} = {result} - {odd_or_even}")
elif user_operator == '/' and number_one != 0 and number_two != 0:
    print(f"{number_one} / {number_two} = {result:.2f}")
elif user_operator == '%' and number_one != 0 and number_two != 0:
    print(f"{number_one} % {number_two} = {number_one % number_two}")
