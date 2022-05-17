petar_budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())
video_card = number_of_video_cards * 250
processor = number_of_processors * (video_card * 0.35)
ram = number_of_ram * (video_card * 0.10)
total_sum = video_card + processor + ram
if number_of_video_cards > number_of_processors:
    total_sum -= total_sum * 0.15
diff = abs(total_sum - petar_budget)
if petar_budget > total_sum:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
