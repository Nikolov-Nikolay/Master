destination = input()
date_for_excursion = input()
number_of_nights = int(input())
price = 0

if destination == 'France':
    if date_for_excursion == '21-23':
        price = 30
    elif date_for_excursion == '24-27':
        price = 35
    elif date_for_excursion == '28-31':
        price = 40
elif destination == 'Italy':
    if date_for_excursion == '21-23':
        price = 28
    elif date_for_excursion == '24-27':
        price = 32
    elif date_for_excursion == '28-31':
        price = 39
elif destination == 'Germany':
    if date_for_excursion == '21-23':
        price = 32
    elif date_for_excursion == '24-27':
        price = 37
    elif date_for_excursion == '28-31':
        price = 43

price_for_excursion = price * number_of_nights
print(f"Easter trip to {destination} : {price_for_excursion:.2f} leva.")
