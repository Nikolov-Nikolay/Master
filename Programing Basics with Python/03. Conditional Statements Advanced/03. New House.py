type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())
costs = - 1.0
if type_of_flower == "Roses":
    costs = number_of_flowers * 5
    if number_of_flowers > 80:
        costs -= costs * 0.10

elif type_of_flower == "Dahlias":
    costs = number_of_flowers * 3.80
    if number_of_flowers > 90:
        costs -= costs * 0.15

elif type_of_flower == "Tulips":
    costs = number_of_flowers * 2.80
    if number_of_flowers > 80:
        costs -= costs * 0.15

elif type_of_flower == "Narcissus":
    costs = number_of_flowers * 3
    if number_of_flowers < 120:
        costs += costs * 0.15

elif type_of_flower == "Gladiolus":
    costs = number_of_flowers * 2.50
    if number_of_flowers < 80:
        costs += costs * 0.20

diff = abs(budget - costs)
if budget >= costs:
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {diff:.2f} leva left.')

else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
