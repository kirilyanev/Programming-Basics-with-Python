actor_name = input()
academy_points = float(input())
judges = int(input())

actor_points = academy_points

for i in range(1, judges + 1):
    judge_name = input()
    judge_points = float(input())
    actor_points += len(judge_name) * judge_points / 2
    if actor_points > 1250.5:
        break

if actor_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - actor_points:.1f} more!")
