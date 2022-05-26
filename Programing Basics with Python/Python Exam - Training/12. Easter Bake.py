import math

number_of_easter_cake = int(input())
all_used_sugar = 0
all_used_flour = 0
max_flour = 0
max_sugar = 0

for cake in range(1, number_of_easter_cake + 1):
    used_sugar = int(input())
    used_flour = int(input())
    if used_flour > max_flour:
        max_flour = used_flour
    if used_sugar > max_sugar:
        max_sugar = used_sugar

    all_used_sugar += used_sugar
    all_used_flour += used_flour
packet_of_sugar = math.ceil(all_used_sugar / 950)
packet_of_flour = math.ceil(all_used_flour / 750)
print(f"Sugar: {packet_of_sugar}")
print(f"Flour: {packet_of_flour}")
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
