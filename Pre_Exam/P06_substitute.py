K = int(input())
L = int(input())
M = int(input())
N = int(input())

substitute_count = 0

for num1 in range(K, 8 + 1):
    for num2 in range(9, L - 1, -1):
        for num3 in range(M, 8 + 1):
            for num4 in range(9, N - 1, - 1):
                if num4 % 2 != 0 and num3 % 2 == 0 and num2 % 2 != 0 and num1 % 2 == 0:
                    if num1 != num3 or num2 != num4:
                        substitute_count += 1
                        if substitute_count > 6:
                            break
                        print(f"{num1}{num2} - {num3}{num4}")
                    elif num1 == num3 and num2 == num4:
                        if substitute_count < 6:
                            print(f"Cannot change the same player.")
