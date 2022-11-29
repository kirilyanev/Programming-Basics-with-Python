N = int(input())  # strana_ploshtadka
W = float(input())  # plochka_shirina
L = float(input())  # plochka_daljina
M = int(input())  # peika_shirina
o = int(input())  # peika_dyljina

lice_ploshtadka = N * N
lice_plochka = W * L
lice_peika = M * o

final_ploshtadka = lice_ploshtadka - lice_peika
plochki_broi = final_ploshtadka / lice_plochka
time = plochki_broi * 0.2

print(round(plochki_broi, 2))
print(round(time, 2))
