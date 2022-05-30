import math

breed_of_cat = input()
gender_of_cat = input()
cat_years = 0
cats_months = 0

if gender_of_cat == 'm':
    if breed_of_cat == 'British Shorthair':
        cat_years = 13
    elif breed_of_cat == 'Siamese':
        cat_years = 15
    elif breed_of_cat == 'Persian':
        cat_years = 14
    elif breed_of_cat == "Ragdoll":
        cat_years = 16
    elif breed_of_cat == 'American Shorthair':
        cat_years = 12
    elif breed_of_cat == 'Siberian':
        cat_years = 11

elif gender_of_cat == 'f':
    if breed_of_cat == 'British Shorthair':
        cat_years = 14
    elif breed_of_cat == 'Siamese':
        cat_years = 16
    elif breed_of_cat == 'Persian':
        cat_years = 15
    elif breed_of_cat == "Ragdoll":
        cat_years = 17
    elif breed_of_cat == 'American Shorthair':
        cat_years = 13
    elif breed_of_cat == 'Siberian':
        cat_years = 12

if breed_of_cat == "British Shorthair":
    human_months = cat_years * 12
    cats_months = math.floor(human_months / 6)
    print(f'{cats_months} cat months')
elif breed_of_cat == "Siamese":
    human_months = cat_years * 12
    cats_months = math.floor(human_months / 6)
    print(f'{cats_months} cat months')
elif breed_of_cat == "Persian":
    human_months = cat_years * 12
    cats_months = math.floor(human_months / 6)
    print(f'{cats_months} cat months')
elif breed_of_cat == "Ragdoll":
    human_months = cat_years * 12
    cats_months = math.floor(human_months / 6)
    print(f'{cats_months} cat months')
elif breed_of_cat == "American Shorthair":
    human_months = cat_years * 12
    cats_months = math.floor(human_months / 6)
    print(f'{cats_months} cat months')
elif breed_of_cat == "Siberian":
    human_months = cat_years * 12
    cats_months = math.floor(human_months / 6)
    print(f'{cats_months} cat months')
else:
    print(f'{breed_of_cat} is invalid cat!')


