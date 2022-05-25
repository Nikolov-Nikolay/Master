import sys

name_of_player = input()
number_of_goals = int(input())
max_goals = - sys.maxsize

while name_of_player != 'End':
    if number_of_goals >= 3:
        max_goals = number_of_goals
    elif number_of_goals != 3:
        max_goals = number_of_goals
       