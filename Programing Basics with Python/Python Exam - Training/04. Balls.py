number_of_balls = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_colors_picked = 0
divided_from_black_balls = 0
for n in range(number_of_balls):
    colors_of_balls = input()
    if colors_of_balls == 'red':
        points += 5
        red_balls += 1
    elif colors_of_balls == 'orange':
        points += 10
        orange_balls += 1
    elif colors_of_balls == 'yellow':
        points += 15
        yellow_balls += 1
    elif colors_of_balls == 'white':
        points += 20
        white_balls += 1
    if colors_of_balls == 'black':
        points /= 2
        divided_from_black_balls += 1
    if colors_of_balls != 'red' and colors_of_balls != 'orange' and colors_of_balls != 'yellow' \
            and colors_of_balls != 'white' and colors_of_balls != 'black':
        other_colors_picked += 1

print(f"Total points: {int(points)}")
print(f"Red balls: {red_balls}")
print(f'Orange balls: {orange_balls}')
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colors_picked}")
print(f"Divides from black balls: {divided_from_black_balls}")


