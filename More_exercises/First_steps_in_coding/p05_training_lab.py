import math

w = float(input()) * 100
h = float(input()) * 100
roll = w / 120
column = (h - 100) / 70

seats = math.trunc(roll) * math.trunc(column) - 3

print(seats)
