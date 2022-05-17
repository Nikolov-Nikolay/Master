budget_of_group = int(input())
season = input()
number_of_fishers = int(input())
rent_of_ship = 0

if season == "Spring":
    rent_of_ship = 3000
elif season == "Summer":
    rent_of_ship = 4200
elif season == "Autumn":
    rent_of_ship = 4200
elif season == "Winter":
    rent_of_ship = 2600
if number_of_fishers <= 6:
    rent_of_ship -= rent_of_ship * 0.10
elif 7 <= number_of_fishers <= 11:
    rent_of_ship -= rent_of_ship * 0.15
elif number_of_fishers >= 12:
    rent_of_ship -= rent_of_ship * 0.25
if season != 'Autumn':
    if number_of_fishers % 2 == 0:
        rent_of_ship -= rent_of_ship * 0.05
diff = abs(budget_of_group - rent_of_ship)
if budget_of_group > rent_of_ship:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')