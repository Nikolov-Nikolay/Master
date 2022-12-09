pairs = int(input())
students_book = {}

for i in range(pairs):
    name = input()
    grade = float(input())

    if name not in students_book:
        students_book[name] = [grade]
    else:
        students_book[name].append(grade)

[print(f"{name} -> {(sum(value) / len(value)):.2f}")
 for name, value in students_book.items() if (sum(value) / len(value)) >= 4.5]
