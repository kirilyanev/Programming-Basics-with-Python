students_count = int(input())

average_grade = 0
group_one = 0
group_two = 0
group_three = 0
group_four = 0

for student in range(1, students_count + 1):
    grade = float(input())
    if grade >= 5.00:
        group_one += 1
        average_grade += grade
    elif 4.00 <= grade <= 4.99:
        group_two += 1
        average_grade += grade
    elif 3.00 <= grade <= 3.99:
        group_three += 1
        average_grade += grade
    elif grade < 3.00:
        group_four += 1
        average_grade += grade

print(f"Top students: {group_one / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {group_two / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {group_three / students_count * 100:.2f}%")
print(f"Fail: {group_four / students_count * 100:.2f}%")
print(f"Average: {average_grade / students_count:.2f}")
