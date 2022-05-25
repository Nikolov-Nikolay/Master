number_of_bitcoins = int(input())
number_of_chinese_money = int(input())
commission = float(input())

bitcoin = 1168
dollar = 1.76
chinese = 0.15 * dollar
euro = 1.95

price_for_bitcoins = bitcoin * number_of_bitcoins
price_for_chinese = chinese * number_of_chinese_money
budget = (price_for_bitcoins + price_for_chinese) / euro
final_commission = (commission * budget) / 100
final_budget = budget - final_commission
print(f'{final_budget:.2f}')

