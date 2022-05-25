number_of_joinery = int(input())
kind_of_joinery = input()
kind_of_delivery = input()
price_for_kind = 0

if kind_of_joinery == "90x130":
    price_for_kind += 110
elif kind_of_joinery == '100x150':
    price_for_kind += 140
elif kind_of_joinery == '130x180':
    price_for_kind += 190
elif kind_of_joinery == '200x300':
    price_for_kind += 250
print(price_for_kind)

