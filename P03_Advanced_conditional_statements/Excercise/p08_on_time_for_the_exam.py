hour_of_exam = int(input())
minutes_of_exam = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = hour_of_exam * 60 + minutes_of_exam
arrival_time = arrival_hour * 60 + arrival_minutes

time_difference = abs(exam_time - arrival_time)
hours = time_difference // 60
minutes = time_difference % 60

if exam_time < arrival_time:
    print("Late")
elif exam_time >= arrival_time and time_difference <= 30:
    print("On time")
elif exam_time > arrival_time and time_difference > 30:
    print("Early")

if time_difference >= 1:
    if exam_time > arrival_time and time_difference < 60:
        print(f"{minutes} minutes before the start")
    elif exam_time > arrival_time and time_difference >= 60:
        print(f"{hours}:{minutes:02d} hours before the start")
    elif exam_time < arrival_time and time_difference < 60:
        print(f"{minutes} minutes after the start")
    elif exam_time < arrival_time and time_difference >= 60:
        print(f"{hours}:{minutes:02d} hours after the start")
