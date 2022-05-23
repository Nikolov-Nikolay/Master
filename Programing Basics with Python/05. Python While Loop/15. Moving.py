width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())
number_of_box = 0
free_space = width_of_free_space * length_of_free_space * height_of_free_space

while True:
    current_number_of_box = input()

    if current_number_of_box == 'Done':
        break
    number_of_box += int(current_number_of_box)

    if number_of_box > free_space:
        break
diff = abs(number_of_box - free_space)

if number_of_box <= free_space:
    print(f'{diff} Cubic meters left.')
else:
    print(f'No more free space! You need {diff} Cubic meters more.')
