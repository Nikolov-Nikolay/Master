minutes_for_walking = int(input())
number_of_walking_in_day = int(input())
calories_in_day = int(input())

total_minutes_for_walking_in_day = minutes_for_walking * number_of_walking_in_day
calories_deficit = total_minutes_for_walking_in_day * 5
number_calories_in_day = (calories_in_day * 50) / 100

if calories_deficit > number_calories_in_day:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_deficit}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_deficit}.')
