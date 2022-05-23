import sys

command = input()
max_number = -sys.maxsize
while command != "Stop":
    number = int(command)
    if number > max_number:
        max_number = number
    command = input()
else:
    print(max_number)
