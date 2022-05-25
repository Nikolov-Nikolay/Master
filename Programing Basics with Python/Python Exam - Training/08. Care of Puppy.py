food_buy_for_dog_in_kilos = int(input())
grams_for_each_eat = input()
total_eaten_food = 0

food_buy_for_dog_in_grams = food_buy_for_dog_in_kilos * 1000
while grams_for_each_eat != 'Adopted':
    grams_for_each_eat_puppy = int(grams_for_each_eat)
    total_eaten_food += grams_for_each_eat_puppy
    grams_for_each_eat = input()
left_food = abs(food_buy_for_dog_in_grams - total_eaten_food)
if left_food <= food_buy_for_dog_in_grams:
    print(f'Food is enough! Leftovers: {left_food} grams.')
else:
    print(f'Food is not enough. You need {left_food} grams more.')