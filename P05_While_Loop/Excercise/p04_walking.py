steps = input()
walked_steps = 0

while steps != 'Going home':
    steps = int(steps)
    walked_steps += steps
    if walked_steps >= 10000:
        break
    steps = input()

if steps == "Going home":
    walked_steps_to_home = int(input())
    walked_steps += walked_steps_to_home

diff_step = abs(walked_steps - 10000)

if walked_steps < 10000:
    print(f"{diff_step} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{diff_step} steps over the goal!")
