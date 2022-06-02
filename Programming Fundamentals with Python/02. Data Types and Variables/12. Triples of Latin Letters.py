number = int(input())

for i in range(number):
    for a in range(number):
        for b in range(number):
            print(f'{chr(97 + i)}{chr(97 + a)}{chr(97 + b)}')
