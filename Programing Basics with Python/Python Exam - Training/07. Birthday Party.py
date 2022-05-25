rent_for_hall = float(input())

price_for_cake = (rent_for_hall * 20) / 100
price_for_drinks = price_for_cake - (price_for_cake * 45) / 100
price_for_animator = (rent_for_hall / 3)

need_money = rent_for_hall + price_for_cake + price_for_drinks + price_for_animator
print(need_money)
