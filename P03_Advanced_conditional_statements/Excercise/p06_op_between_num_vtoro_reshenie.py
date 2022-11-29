n1 = int(input())
n2 = int(input())
operator = input()

answer = ''
result = 0

if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        answer = 'even'
    else:
        answer = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {answer}')
elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        answer = 'even'
    else:
        answer = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {answer}')
elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        answer = 'even'
    else:
        answer = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {answer}')

elif operator == '/':
    if n1 != 0 and n2 != 0:
        result = n1 / n2
        print(f'{n1} {operator} {n2} = {result:.2f}')
    else:
        print(f"Cannot divide {n1} by zero")

elif operator == '%':
    if n1 != 0 and n2 != 0:
        result = n1 % n2
        print(f'{n1} {operator} {n2} = {result}')
    else:
        print(f"Cannot divide {n1} by zero")