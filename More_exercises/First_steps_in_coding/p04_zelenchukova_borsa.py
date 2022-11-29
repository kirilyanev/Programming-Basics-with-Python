price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

total_sum = ((price_vegetables * kg_vegetables) + (price_fruits * kg_fruits)) / 1.94

print("{:.2f}".format(total_sum))
