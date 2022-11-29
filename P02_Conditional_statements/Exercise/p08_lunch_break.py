from math import ceil

serial = input()
episode_lenght = int(input())
lunch_break = int(input())

lunch = 0.125 * lunch_break
rest = 0.25 * lunch_break
time_left = lunch_break - lunch - rest

if time_left >= episode_lenght:
    print(f"You have enough time to watch {serial} and left with {ceil(time_left - episode_lenght)}"
          f" minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {ceil(episode_lenght - time_left)}"
          f" more minutes.")
