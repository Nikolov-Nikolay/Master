budget_for_movie = float(input())
number_of_statist = int(input())
price_for_clothes_for_one_statist = float(input())
discount = 0

decor_for_movie = budget_for_movie * 10 / 100
price_for_clothes = price_for_clothes_for_one_statist * number_of_statist
full_price_for_movie = decor_for_movie + price_for_clothes
final_price_for_movie = budget_for_movie - full_price_for_movie

if number_of_statist > 150:
    discount = price_for_clothes - (price_for_clothes * 10) / 100
    final_price_for_movie = final_price_for_movie - discount

if final_price_for_movie < budget_for_movie:
    print(f'Action! Wingard starts filming with {final_price_for_movie:.2f} leva left.')
else:
    print(f'Not enough money! Wingard needs {abs(final_price_for_movie):.2f} leva more.')
