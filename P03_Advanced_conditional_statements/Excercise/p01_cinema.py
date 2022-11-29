projection = input()
rows = int(input())
columns = int(input())

tickets = rows * columns

if projection == "Premiere":
    print(f"{12 * tickets:.2f} leva")
elif projection == "Normal":
    print(f"{7.50 * tickets:.2f} leva")
elif projection == "Discount":
    print(f"{5 * tickets:.2f} leva")
