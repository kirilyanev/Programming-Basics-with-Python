packets_pens = int(input())
packets_markers = int(input())
cleaning_agent_liters = int(input())
discount_percent = int(input()) / 100

final_sum = (packets_pens * 5.80) + (packets_markers * 7.20) + (cleaning_agent_liters * 1.20)
discount = final_sum * discount_percent
final_sum_with_discount = final_sum - discount

print(final_sum_with_discount)
