name_of_student = input()
grades = 1.0
sum_grades = 0
excluded = 1
average = 0
while grades <= 12:
    grade = float(input())
    if grade < 4.00:
        print(f"{name_of_student} has been excluded at {excluded} grade")
        break
    else:
        grades += 1
        excluded += 1
        sum_grades += grade
else:
    average = sum_grades / 12
    print(f"{name_of_student} graduated. Average grade: {average:.2f}")
