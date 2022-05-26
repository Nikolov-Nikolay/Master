import math

number_of_guests = int(input())
budget = int(input())

number_of_need_easter_bread = math.ceil(number_of_guests / 3)
number_of_need_eggs = number_of_guests * 2
price_for_easter_bread = number_of_need_easter_bread * 4
price_for_eggs = number_of_need_eggs * 0.45
full_price = price_for_eggs + price_for_easter_bread
diff = budget - full_price

if budget >= full_price:
    print(f'Lyubo bought {number_of_need_easter_bread} Easter bread and {number_of_need_eggs} eggs.')
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {abs(diff):.2f} lv. more.")
