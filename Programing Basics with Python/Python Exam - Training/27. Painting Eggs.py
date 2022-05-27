size_of_eggs = input()
color_of_eggs = input()
number_of_batch = int(input())
price_for_one_batch = 0

if size_of_eggs == 'Large':
    if color_of_eggs == 'Red':
        price_for_one_batch = 16
    if color_of_eggs == 'Green':
        price_for_one_batch = 12
    if color_of_eggs == 'Yellow':
        price_for_one_batch = 9
elif size_of_eggs == 'Medium':
    if color_of_eggs == 'Red':
        price_for_one_batch = 13
    if color_of_eggs == 'Green':
        price_for_one_batch = 9
    if color_of_eggs == 'Yellow':
        price_for_one_batch = 7
elif size_of_eggs == 'Small':
    if color_of_eggs == 'Red':
        price_for_one_batch = 9
    if color_of_eggs == 'Green':
        price_for_one_batch = 8
    if color_of_eggs == 'Yellow':
        price_for_one_batch = 5

price = price_for_one_batch * number_of_batch
costs = price - (price * 35 / 100)
print(f'{costs:.2f} leva.')
