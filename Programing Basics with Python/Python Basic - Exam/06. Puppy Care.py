buyed_food_dog_puppy = int(input())
eaten_food_for_every_time = int(input())
food_for_eat = 0
left_food = 0

buyed_food_dog_puppy_in_grams = buyed_food_dog_puppy * 1000

while eaten_food_for_every_time != 'Adopted':
    food_for_eat += int(str(eaten_food_for_every_time))
    eaten_food_for_every_time = input()
    left_food = buyed_food_dog_puppy_in_grams - food_for_eat
if food_for_eat <= buyed_food_dog_puppy_in_grams:
    print(f'Food is enough! Leftovers: {left_food} grams.')
else:
    print(f'Food is not enough. You need {abs(left_food)} grams more.')