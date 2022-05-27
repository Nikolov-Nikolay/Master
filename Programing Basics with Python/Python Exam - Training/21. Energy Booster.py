fruit = input()
size_of_set = input()
number_of_sets = int(input())
price_for_one_set = 0
discount = 0

if size_of_set == 'small':
    size_of_set = 2
    if fruit == 'Watermelon':
        price_for_one_set = 56
    elif fruit == 'Mango':
        price_for_one_set = 36.66
    elif fruit == 'Pineapple':
        price_for_one_set = 42.10
    elif fruit == 'Raspberry':
        price_for_one_set = 20
if size_of_set == 'big':
    size_of_set = 5
    if fruit == 'Watermelon':
        price_for_one_set = 28.70
    elif fruit == 'Mango':
        price_for_one_set = 19.60
    elif fruit == 'Pineapple':
        price_for_one_set = 24.80
    elif fruit == 'Raspberry':
        price_for_one_set = 15.20
price_for_big_set = size_of_set * price_for_one_set
price_for_all_sets = number_of_sets * price_for_big_set
if 400 <= price_for_all_sets <= 1000:
    discount = (price_for_all_sets * 15) / 100
elif price_for_all_sets > 1000:
    discount = (price_for_all_sets * 50) / 100
final_price = price_for_all_sets - discount

print(f'{final_price:.2f} lv.')
