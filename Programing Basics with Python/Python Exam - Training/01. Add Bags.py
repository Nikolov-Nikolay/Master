price_for_bags_upper_than_20 = float(input())
kilos_for_bags = float(input())
days_to_trip = int(input())
number_of_bags = int(input())
price_for_bags = 0
if kilos_for_bags < 10:
    price_for_bags = (price_for_bags_upper_than_20 * 20) / 100
elif 10 <= kilos_for_bags <= 20:
    price_for_bags = (price_for_bags_upper_than_20 * 50) / 100
elif kilos_for_bags > 20:
    price_for_bags = price_for_bags_upper_than_20
if days_to_trip > 30:
    percent_of_price_for_bags = (price_for_bags * 10) / 100
elif 7 < days_to_trip <= 30:
    percent_of_price_for_bags = (price_for_bags * 15) / 100
elif days_to_trip < 7:
    percent_of_price_for_bags = (price_for_bags * 40) / 100

full_price_for_bags = (price_for_bags + percent_of_price_for_bags) * number_of_bags
print(f" The total price of bags is: {full_price_for_bags:.2f} lv. ")

