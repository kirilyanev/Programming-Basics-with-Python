sea_packages = int(input())
mountain_packages = int(input())

income = 0
package_name = input()

while package_name != "Stop":
    if package_name == "sea" and sea_packages > 0:
        income += 680
        sea_packages -= 1
    elif package_name == "mountain" and mountain_packages > 0:
        income += 499
        mountain_packages -= 1
    if sea_packages + mountain_packages == 0:
        break
    package_name = input()

if sea_packages == 0 and mountain_packages == 0:
    print(f" Good job! Everything is sold.")

print(f"Profit: {income} leva.")
