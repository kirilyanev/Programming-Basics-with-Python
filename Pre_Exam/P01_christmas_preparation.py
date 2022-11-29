paper_rolls = int(input())
fabric_rolls = int(input())
glue_liters = float(input())
discount_percent = int(input())

paper = 5.80
fabric = 7.20
glue = 1.20

paper_price = paper_rolls * paper
fabric_price = fabric_rolls * fabric
glue_price = glue_liters * glue

materials_sum = paper_price + fabric_price + glue_price
total_sum = materials_sum - (materials_sum * discount_percent/100)

print(f'{total_sum:.3f}')
