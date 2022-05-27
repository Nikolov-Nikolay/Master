airplane_capacity = float(input())
counter = 0

while True:
    suitcase = input()

    if suitcase == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        suitcase = float(suitcase)

    if (counter + 1) % 3 == 0:
        suitcase *= 1.1

    if suitcase > airplane_capacity:
        print("No more space!")
        break

    counter += 1
    airplane_capacity -= suitcase

print(f'Statistic: {counter} suitcases loaded.')
