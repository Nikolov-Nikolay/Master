number_of_location = int(input())
mine_gold = 0

for location in range(1, number_of_location + 1):
    expect_gold = int(input())
    number_of_days = int(input())
    for gold in range(1, number_of_days +1):
        gold = int(input())
        mine_gold += gold
    average_gold = mine_gold / number_of_days
    mine_gold = 0
    if average_gold >= expect_gold:
        print(f'Good job! Average gold per day: {average_gold:.2f}.')
    else:
        print(f'You need {expect_gold - average_gold:.2f} gold.')

