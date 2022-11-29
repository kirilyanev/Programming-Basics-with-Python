from math import floor

all_tournaments = int(input())
ranking_points = int(input())

points = 0
win = 0

for i in range(1, all_tournaments + 1):
    tournament_phase = input()
    if tournament_phase == "W":
        points += 2000
        win += 1
    elif tournament_phase == "F":
        points += 1200
    elif tournament_phase == "SF":
        points += 720

tournament_average_points = floor(points / all_tournaments)
percentage_tournaments_won = win / all_tournaments * 100

print(f"Final points: {points + ranking_points}")
print(f"Average points: {tournament_average_points}")
print(f"{percentage_tournaments_won:.2f}%")