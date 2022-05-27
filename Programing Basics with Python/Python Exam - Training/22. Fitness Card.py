budget = float(input())
gender = input()
age = int(input())
sport = input()
price_for_card = 0
discount = 0

if gender == 'm':
    if sport == 'Gym':
        price_for_card = 42
    elif sport == 'Boxing':
        price_for_card = 41
    elif sport == 'Yoga':
        price_for_card = 45
    elif sport == 'Zumba':
        price_for_card = 34
    elif sport == 'Dances':
        price_for_card = 51
    elif sport == 'Pilates':
        price_for_card = 39
elif gender == 'f':
    if sport == 'Gym':
        price_for_card = 35
    elif sport == 'Boxing':
        price_for_card = 37
    elif sport == 'Yoga':
        price_for_card = 42
    elif sport == 'Zumba':
        price_for_card = 31
    elif sport == 'Dances':
        price_for_card = 53
    elif sport == 'Pilates':
        price_for_card = 37
if age <= 19:
    discount = (price_for_card * 20) / 100
money = (price_for_card - discount) - budget
final_price = price_for_card - discount

if budget >= final_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${money:.2f} more.")
