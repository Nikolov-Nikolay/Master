import math

number_of_processors_to_make_it = int(input())
number_of_workers = int(input())
working_days = int(input())

working_hours = number_of_workers * 8 * working_days
processors_made = math.floor(working_hours / 3)

if processors_made < number_of_processors_to_make_it:
    diff = number_of_processors_to_make_it - processors_made
    losses = diff * 110.10
    print(f'Losses: -> {losses:.2f} BGN')
else:
    win = processors_made - number_of_processors_to_make_it
    profit = win * 110.10
    print(f'Profit: -> {profit:.2f} BGN')