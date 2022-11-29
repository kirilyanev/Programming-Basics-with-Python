budget = float(input())
gpus = int(input())
cpus = int(input())
ram = int(input())

gpu_price = 250
cpu_price = 0.35 * (gpu_price * gpus)
ram_price = 0.10 * (gpu_price * gpus)

checkout_price = gpus * gpu_price + cpus * cpu_price + ram * ram_price
discount = 0.15 * checkout_price

if gpus > cpus:
    checkout_price -= discount

if budget >= checkout_price:
    print(f"You have {budget - checkout_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {checkout_price - budget:.2f} leva more!")
