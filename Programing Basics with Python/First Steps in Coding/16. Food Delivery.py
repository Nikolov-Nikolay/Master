chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())
sum_chicken_menu = chicken_menu * 10.35
sum_fish_menu = fish_menu * 12.40
sum_veggie_menu = veggie_menu * 8.15
sum_all_menu = sum_chicken_menu + sum_fish_menu + sum_veggie_menu
dessert = 0.20 * sum_all_menu
total_sum = sum_all_menu + 2.50 + dessert
print(total_sum)

