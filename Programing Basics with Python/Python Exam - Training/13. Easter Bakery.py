price_for_flour_for_one_kilo = float(input())
flour_kilos = float(input())
sugar_kilos = float(input())
number_of_eggs = int(input())
yeast_pack = int(input())

price_for_sugar = price_for_flour_for_one_kilo -  (price_for_flour_for_one_kilo * 25 / 100)
price_for_eggs = price_for_flour_for_one_kilo + (price_for_flour_for_one_kilo * 10 / 100)
price_for_yeast = price_for_sugar - (price_for_sugar * 80 / 100)

amount_for_flour = price_for_flour_for_one_kilo * flour_kilos
amount_for_sugar = price_for_sugar * sugar_kilos
amount_for_eggs = price_for_eggs * number_of_eggs
amount_for_yeast = price_for_yeast * yeast_pack

full_price = amount_for_yeast + amount_for_eggs + amount_for_sugar + amount_for_flour
print(f'{full_price:.2f}')
