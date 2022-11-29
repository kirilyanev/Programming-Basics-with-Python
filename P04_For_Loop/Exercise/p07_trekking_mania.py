groups = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
all_climbers = 0

for i in range(1, groups + 1):
    climbers = int(input())
    all_climbers += climbers
    if climbers <= 5:
        musala += climbers
    elif climbers <= 12:
        montblanc += climbers
    elif climbers <= 25:
        kilimanjaro += climbers
    elif climbers <= 40:
        k2 += climbers
    elif climbers >= 41:
        everest += climbers

print(f"{musala / all_climbers * 100:.2f}%")
print(f"{montblanc / all_climbers * 100:.2f}%")
print(f"{kilimanjaro / all_climbers * 100:.2f}%")
print(f"{k2 / all_climbers * 100:.2f}%")
print(f"{everest / all_climbers * 100:.2f}%")
