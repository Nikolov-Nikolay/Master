age_of_lily = int(input())
washing_machine_price = float(input())
price_for_toy = int(input())
saved_money = 0
number_of_toys = 0

for num in range(1, age_of_lily + 1):
    if num % 2 == 0:
        saved_money += ((num / 2) * 10) -1
    else:
        number_of_toys += 1

total_save_money = saved_money + (number_of_toys * price_for_toy)
diff = abs(total_save_money - washing_machine_price)
if total_save_money >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
