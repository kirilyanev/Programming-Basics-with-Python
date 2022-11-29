price_skum = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

price_palamud = price_skum * 1.6
price_safrid = price_caca * 1.8
price_midi = 7.50

smetka = (price_palamud * kg_palamud) + (price_safrid * kg_safrid) + (price_midi * kg_midi)

print("{:.2f}".format(smetka))
