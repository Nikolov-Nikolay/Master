number_of_cats = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
all_eaten_food = 0

for i in range(1, number_of_cats +1):
    i = int(input())
    if 100 <= i < 200:
        group_1 += 1
        all_eaten_food += i
    elif 200 <= i < 300:
        group_2 += 1
        all_eaten_food += i
    elif 300 <= i < 400:
        group_3 += 1
        all_eaten_food += i
all_eaten_food = all_eaten_food / 1000
price_for_cats_food = all_eaten_food * 12.45
print(f'Group 1: {group_1} cats.')
print(f'Group 2: {group_2} cats.')
print(f'Group 3: {group_3} cats.')
print(f'Price for food per day: {price_for_cats_food:.2f} lv.')