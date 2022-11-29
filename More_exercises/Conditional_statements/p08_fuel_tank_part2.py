type_of_fuel = input()
liters_fuel = float(input())
clubcard = input()

gasoline = 2.22 * liters_fuel
diesel = 2.33 * liters_fuel
gas = 0.93 * liters_fuel

if clubcard == "Yes":
    gasoline -= 0.18 * liters_fuel
    diesel -= 0.12 * liters_fuel
    gas -= 0.08 * liters_fuel

if liters_fuel > 25:
    gasoline -= 0.10 * gasoline
    diesel -= 0.10 * diesel
    gas -= 0.10 * gas
elif 20 <= liters_fuel <= 25:
    gasoline -= 0.08 * gasoline
    diesel -= 0.08 * diesel
    gas -= 0.08 * gas

if type_of_fuel == "Gasoline":
    print(f"{gasoline:.2f} lv.")
elif type_of_fuel == "Diesel":
    print(f"{diesel:.2f} lv.")
elif type_of_fuel == "Gas":
    print(f"{gas:.2f} lv.")
