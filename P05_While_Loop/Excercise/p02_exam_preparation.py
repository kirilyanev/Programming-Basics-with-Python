max_bad_grades = int(input())
problem_name = input()
grade = int(input())

problem_cnt = 0
grades_cnt = 0
grades_sum = 0
bad_grades_cnt = 0
last_problem = ''

while True:
    problem_cnt += 1
    grades_cnt += 1
    grades_sum += grade
    last_problem = problem_name
    if grade <= 4:
        bad_grades_cnt += 1
        if bad_grades_cnt >= max_bad_grades:
            break
    problem_name = input()
    if problem_name == 'Enough':
        break
    grade = int(input())

average_grade = grades_sum / grades_cnt

if problem_name == 'Enough':
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {grades_cnt}")
    print(f"Last problem: {last_problem}")
elif bad_grades_cnt >= max_bad_grades:
    print(f"You need a break, {bad_grades_cnt} poor grades.")
