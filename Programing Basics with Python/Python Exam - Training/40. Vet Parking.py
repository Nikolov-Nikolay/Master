number_of_days = int(input())
number_of_hours_for_everyday = int(input())
price_for_parking = 0
price_for_everyday = 0
day = 0
for number_of_days in range(1, number_of_days + 1):
    day += 1
    for number_of_hours_for_everyday in range(1, number_of_hours_for_everyday + 1):
        if number_of_days % 2 == 0:
            if number_of_hours_for_everyday % 2 == 0:
                price_for_parking += 1
                price_for_everyday += 1
            else:
                price_for_parking += 2.50
                price_for_everyday += 2.50
        else:
            if number_of_hours_for_everyday % 2 == 0:
                price_for_parking += 1.25
                price_for_everyday += 1.25
            else:
                price_for_parking += 1
                price_for_everyday += 1
    print(f"Day: {day} - {price_for_everyday:.2f} leva")
    price_for_everyday = 0
print(f"Total: {price_for_parking:.2f} leva")