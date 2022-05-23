import sys

command = input()
min_number = sys.maxsize
while command != "Stop":
    number = int(command)
    if number < min_number:
        min_number = number
    command = input()
else:
    print(min_number)
