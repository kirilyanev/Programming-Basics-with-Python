tank_lenght = int(input())
tank_width = int(input())
tank_height = int(input())
used_volume_in_percentages = float(input()) / 100

tank_volume_in_centimeters = tank_lenght * tank_width * tank_height
tank_volume_in_liters = tank_volume_in_centimeters / 1000

used_water_volume_in_liters = used_volume_in_percentages * tank_volume_in_liters

needed_water_in_liters = tank_volume_in_liters - used_water_volume_in_liters

print(needed_water_in_liters)
