name_of_actors = input()
points_from_academy = float(input())
number_of_jury = int(input())
points = 0
total_points = 0
for _ in range(number_of_jury):
    name_of_jury = input()
    points_from_jury = float(input())
    points = ((len(name_of_jury) * points_from_jury) / 2)
    total_points += points
    if total_points == 1250.5:
        break
total_points += points_from_academy
diff = 1250.5 - total_points
if total_points >= 1250.5:
    print(f"Congratulations, {name_of_actors} got a nominee for leading role with {abs(total_points)}!")
else:
    print(f'Sorry, {name_of_actors} you need {abs(diff)} more!')
