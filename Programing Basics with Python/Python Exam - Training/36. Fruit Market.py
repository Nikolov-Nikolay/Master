price_for_strawberries = float(input())
bananas_in_kilos = float(input())
oranges_in_kilos = float(input())
raspberries_in_kilos = float(input())
strawberries_in_kilos = float(input())

price_for_raspberries = price_for_strawberries / 2
price_for_oranges = price_for_raspberries - (price_for_raspberries * 40) / 100
price_for_bananas = price_for_raspberries - (price_for_raspberries * 80) / 100
needed_money_for_strawberries = price_for_strawberries * strawberries_in_kilos
needed_money_for_oranges = price_for_oranges * oranges_in_kilos
needed_money_for_raspberries = price_for_raspberries * raspberries_in_kilos
needed_money_for_bananas = price_for_bananas * bananas_in_kilos

needed_money = needed_money_for_strawberries + needed_money_for_oranges + needed_money_for_raspberries \
               + needed_money_for_bananas
print(f'{needed_money:.2f}')
