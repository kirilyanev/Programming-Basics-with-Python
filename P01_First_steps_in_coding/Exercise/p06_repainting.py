nylon = int(input())
paint_in_liters = int(input())
thinner_in_liters = int(input())
work_hours = int(input())

#Prices for materials
price_nylon = 1.50
price_paint = 14.50
price_thinner = 5.00
price_for_additional_materials = ((0.10 * paint_in_liters) * price_paint) + (2 * price_nylon) + 0.40
total_price_for_materials = (nylon * price_nylon) + (paint_in_liters * price_paint) +\
                            (thinner_in_liters * price_thinner) + price_for_additional_materials
price_per_hours_work = (0.30 * total_price_for_materials) * work_hours

total_expenses = total_price_for_materials + price_per_hours_work

print(total_expenses)
