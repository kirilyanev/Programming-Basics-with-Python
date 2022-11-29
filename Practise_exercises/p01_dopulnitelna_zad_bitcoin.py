bitcoin = int(input())
cny = float(input())
commision = float(input()) / 100

bitcoin_to_leva = bitcoin * 1168
cny_to_usd = cny * 0.15
usd_to_leva = cny_to_usd * 1.76
leva_to_euro = (bitcoin_to_leva + usd_to_leva) / 1.95

commision_euro = leva_to_euro * commision
final_sum_euro = leva_to_euro - commision_euro

print(f"{final_sum_euro:.2f}")
