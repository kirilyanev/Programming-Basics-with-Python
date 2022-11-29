weather_degrees = float(input())
if weather_degrees >= 5 and weather_degrees <= 11.9:
    print("Cold")
elif weather_degrees >= 12 and weather_degrees <= 14.9:
    print("Cool")
elif weather_degrees >= 15 and weather_degrees <= 20:
    print("Mild")
elif weather_degrees >= 20.1 and weather_degrees <= 25.9:
    print("Warm")
elif weather_degrees >= 26 and weather_degrees <= 35:
    print("Hot")
else:
    print("unknown")
