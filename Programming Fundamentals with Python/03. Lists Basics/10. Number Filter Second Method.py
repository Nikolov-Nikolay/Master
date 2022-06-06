number = int(input())

positive = list()
negative = list()
odd = list()
even = list()

for i in range(number):
    current = int(input())
    if current % 2 == 0:
        even.append(current)
    else:
        odd.append(current)
    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)

filtered_word = input()

if filtered_word == 'even':
    print(even)
if filtered_word == 'odd':
    print(odd)
if filtered_word == 'positive':
    print(positive)
if filtered_word == 'negative':
    print(negative)
