import re

text = input()
regex = r'([=/])([A-Z][A-Za-z]{2,})\1'

matches = re.finditer(regex, text)
location = list()
points = 0

for match in matches:
    city = match[2]
    location.append(city)
    points += len(city)

output_location = ', '.join(location)
print(f'Destination: {output_location}')
print(f'Travel points: {points}')
