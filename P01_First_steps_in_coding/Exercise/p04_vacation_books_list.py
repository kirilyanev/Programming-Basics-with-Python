pages_num = int(input())
pages_for_one_hour = int(input())
days = int(input())

hours_per_day = (pages_num // pages_for_one_hour) // days

print(hours_per_day)