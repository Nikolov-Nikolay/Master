price_for_one_year_subscription = int(input())

price_for_sneakers = price_for_one_year_subscription - (price_for_one_year_subscription * 40 / 100)
price_for_outfit = price_for_sneakers - (price_for_sneakers * 20) / 100
price_for_ball = price_for_outfit / 4
price_for_accessories = price_for_ball / 5

full_price_for_equipment = price_for_sneakers + price_for_outfit + price_for_ball + price_for_accessories \
                           + price_for_one_year_subscription
print(f'{full_price_for_equipment:.2f}')

