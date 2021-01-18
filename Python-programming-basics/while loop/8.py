name = input()
grade_completed = 1
sum_marks = 0
while grade_completed <= 12:
    mark = float(input())
    if mark >= 4:
        grade_completed += 1
        sum_marks += mark
average_mark = sum_marks / 12
print(f'{name} graduated. Average grade: {average_mark:.2f}')