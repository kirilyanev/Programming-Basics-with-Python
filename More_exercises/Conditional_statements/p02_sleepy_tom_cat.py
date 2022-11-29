rest_days = int(input())

work_days = 365 - rest_days
minutes_of_play = work_days * 63 + rest_days * 127
play_norm_difference = abs(30000 - minutes_of_play)

if minutes_of_play > 30000:
    print("Tom will run away")
    print(f"{play_norm_difference // 60} hours and {play_norm_difference % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{play_norm_difference // 60} hours and {play_norm_difference % 60} minutes less for play")
