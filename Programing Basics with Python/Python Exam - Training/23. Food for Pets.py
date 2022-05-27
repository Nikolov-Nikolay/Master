number_of_days = int(input())
total_food = float(input())
dog = 0
cat = 0
total_eaten_food = 0
biscuits = 0

for everyday in range(1, number_of_days + 1):
    eaten_dog_food = int(input())
    dog += eaten_dog_food
    eaten_cat_food = int(input())
    cat += eaten_cat_food
    total_eaten_food += eaten_dog_food + eaten_cat_food
    if everyday % 3 == 0:
        biscuits += round(((eaten_dog_food + eaten_cat_food) * 0.10))

print(f'Total eaten biscuits: {biscuits}gr.')
print(f"{total_eaten_food / total_food * 100:.2f}% of the food has been eaten.")
print(f"{dog / total_eaten_food * 100:.2f}% eaten from the dog.")
print(f"{cat / total_eaten_food * 100:.2f}% eaten from the cat.")
