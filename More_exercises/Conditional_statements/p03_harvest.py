import math

vineyard = int(input())
grape_for_meter = float(input())
required_liters_vine = int(input())
workers = int(input())

harvest = vineyard * 0.40
grape_kg = harvest * grape_for_meter
required_grape_kg = required_liters_vine * 2.5
produced_liters_vine = grape_kg / 2.5

if produced_liters_vine < required_liters_vine:
    print(f"It will be a tough winter! More {math.floor(required_liters_vine - produced_liters_vine)} "
          f"liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(produced_liters_vine)} liters.")
    print(f"{math.ceil(produced_liters_vine - required_liters_vine)} liters left ->"
          f" {math.ceil((produced_liters_vine - required_liters_vine) / workers)} liters per person.")
