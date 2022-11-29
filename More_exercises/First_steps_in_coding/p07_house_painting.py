# Razmeri na stenite
x = float(input())
y = float(input())
h = float(input())

# steni na kyshtata
predna_stena = x*x - (1.2*2)
zadna_stena = x*x
stranichna_strana = x*y - (1.5*1.5)

# Razmeri na pokriv
pravoygylnik_pokriv = x*y
triygylnik_pokriv = x*h/2

# Plosht kyshta
kyshta = predna_stena + zadna_stena + (2 * stranichna_strana)

# Plosht pokriv
pokriv = (pravoygylnik_pokriv + triygylnik_pokriv) * 2

green_paint = kyshta / 3.4
red_paint = pokriv / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
