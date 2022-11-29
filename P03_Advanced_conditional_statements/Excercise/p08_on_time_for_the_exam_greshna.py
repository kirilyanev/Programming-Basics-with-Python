hour_of_exam = int(input())
minutes_of_exam = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_in_minutes = hour_of_exam * 60 + minutes_of_exam
arrival_time_in_minutes = arrival_hour * 60 + arrival_minutes

time_difference = abs(exam_time_in_minutes - arrival_time_in_minutes)
time_difference_in_minutes = time_difference % 60
time_difference_in_hours = time_difference // 60


if arrival_time_in_minutes > exam_time_in_minutes:
    print("Late")
elif time_difference <= 30:
    print("On time")
elif time_difference > 30:
    print("Early")

if time_difference > 1:
    if exam_time_in_minutes > arrival_time_in_minutes and exam_time_in_minutes - arrival_time_in_minutes < 60:
        print(f"{time_difference_in_minutes} minutes before the start")
    elif exam_time_in_minutes - arrival_time_in_minutes >= 60:
        print(f"{time_difference_in_hours}:{time_difference_in_minutes:02d} hours before the start")
    elif arrival_time_in_minutes - exam_time_in_minutes < 60:
        print(f"{time_difference_in_minutes} minutes after the start")
    elif arrival_time_in_minutes - exam_time_in_minutes >= 60:
        print(f"{time_difference_in_hours}:{time_difference_in_minutes:02d} hours after the start")
