command = input()
total_deposit = 0

while command != "NoMoreMoney":
    command = float(command)
    if command < 0:
        print("Invalid operation!")
        break
    total_deposit += command
    print(f"Increase: {command:.2f}")
    command = input()

print(f"Total: {total_deposit:.2f}")
