number_of_cake = int(input())
number_of_eggs = int(input())
kilos_biscuits = int(input())

price_for_cakes = number_of_cake * 3.20
price_for_eggs = number_of_eggs * 4.35
price_for_biscuits = kilos_biscuits * 5.40
price_for_egg_paint = number_of_eggs * 12 * 0.15

price_for_lunch = price_for_eggs + price_for_egg_paint + price_for_biscuits + price_for_cakes
print(f'{price_for_lunch:.2f}')
