record = float(input())
distance = float(input())
time_for_one_meter = float(input())

swimming_time = distance * time_for_one_meter + (distance // 15) * 12.5

if swimming_time < record:
    print(f"Yes, he succeeded! The new world record is {swimming_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {swimming_time - record:.2f} seconds slower.")
