import math

price_for_one_tennis_rocket = float(input())
number_of_tennis_rocket = int(input())
number_of_pair_sneakers = int(input())

price_for_tennis_rockets = price_for_one_tennis_rocket * number_of_tennis_rocket
price_for_one_pair_sneakers = price_for_one_tennis_rocket / 6
price_for_all_sneakers = number_of_pair_sneakers * price_for_one_pair_sneakers

price_for_equipment = (price_for_tennis_rockets + price_for_all_sneakers) * 20 / 100
full_price = price_for_equipment + price_for_all_sneakers + price_for_tennis_rockets
price_for_djokovic = full_price / 8
price_for_sponsors = full_price * 7 / 8
print(f"Price to be paid by Djokovic {math.floor(price_for_djokovic)}")
print(f"Price to be paid by sponsors {math.ceil(price_for_sponsors)}")

