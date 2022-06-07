def calculator(a, b, operator):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


current_operator = input()
first_num = int(input())
second_num = int(input())

print(calculator(first_num, second_num, current_operator))
# print(calculator(operator='multiply', b=15, a=20)) използва се за тест на входните данни без да се пише инпут в конзолата
# print(calculator(operator=input(), a=int(input()), b=int(input()))) опция за слагането на входните данни на един ред