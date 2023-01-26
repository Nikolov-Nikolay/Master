"""
occurrences_dict
loop values:
    occurrences_dict[value] += 1
"""

numbers_string = input()

occurrences_counts = {}
numbers = [float(x) for x in numbers_string.split(' ')]

for number in numbers:
    if number not in occurrences_counts:
        occurrences_counts[number] = 0
    occurrences_counts[number] += 1

for number, count in occurrences_counts.items():
    print(f'{number:.1f} - {count} times')
