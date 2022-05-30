budget = float(input())
needed_liters_petrol = float(input())
day_of_the_week = input()
discount = 0

price_for_petrol = needed_liters_petrol * 2.10
needed_money = price_for_petrol + 100
if day_of_the_week == 'Saturday':
    discount = needed_money - (needed_money * 10) / 100
elif day_of_the_week == 'Sunday':
    discount = needed_money - (needed_money * 20) / 100
diff = budget - discount
if budget >= discount:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {abs(diff):.2f} lv.')

