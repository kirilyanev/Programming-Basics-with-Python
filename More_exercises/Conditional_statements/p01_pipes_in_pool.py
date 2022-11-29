pool_volume = int(input())
flow_rate_one = int(input())
flow_rate_two = int(input())
hours = float(input())

liters_filled = (flow_rate_one + flow_rate_two) * hours
fill_percentages = liters_filled / pool_volume * 100
pipe_one_percentages = flow_rate_one * hours / liters_filled * 100
pipe_two_percentages = flow_rate_two * hours / liters_filled * 100

if pool_volume >= liters_filled:
    print(f"The pool is {fill_percentages}% full. "
          f"Pipe 1: {pipe_one_percentages:.2f}%. Pipe 2: {pipe_two_percentages:.2f}%.")
else:
    print(f"For {hours} hours the pool "
          f"overflows with {liters_filled - pool_volume} liters.")
