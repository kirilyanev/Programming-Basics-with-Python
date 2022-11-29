student_name = input()

student_not_passing = 0
all_grades = 0
finished_class = 0

while student_not_passing < 2:
    grade = float(input())
    all_grades += grade
    finished_class += 1
    if finished_class == 12:
        break
    if grade < 4:
        student_not_passing += 1
        all_grades -= grade
        finished_class -= 1

current_class = finished_class + 1

if student_not_passing < 2:
    print(f"{student_name} graduated. Average grade: {(all_grades / finished_class):.2f}")
else:
    print(f"{student_name} has been excluded at {current_class} grade")
