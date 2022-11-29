kilometers = int(input())
time_of_day = input()
taxi = 0

if time_of_day == "day":
    taxi = 0.70 + (0.79 * kilometers)
elif time_of_day == "night":
    taxi = 0.70 + (0.90 * kilometers)

if kilometers >= 100:
    print(f"{0.06 * kilometers:.2f}")
elif kilometers >= 20:
    print(f"{0.09 * kilometers:.2f}")
else:
    print(f"{taxi:.2f}")
