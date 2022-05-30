time_for_contract = input()
type_for_contract = input()
mobile_network = input()
number_of_months_to_pay = int(input())
price_for_contract = 0
price_for_mobile_network = 0

if time_for_contract == 'one':
    if type_for_contract == 'Small':
        price_for_contract = 9.98
    elif type_for_contract == 'Middle':
        price_for_contract = 18.99
    elif type_for_contract == 'Large':
        price_for_contract = 25.98
    elif type_for_contract == 'ExtraLarge':
        price_for_contract = 35.99
elif time_for_contract == 'two':
    if type_for_contract == 'Small':
        price_for_contract = 8.58
    elif type_for_contract == 'Middle':
        price_for_contract = 17.09
    elif type_for_contract == 'Large':
        price_for_contract = 23.59
    elif type_for_contract == 'ExtraLarge':
        price_for_contract = 31.79
if mobile_network == 'yes':
    if price_for_contract <= 10:
        price_for_mobile_network = 5.50
    elif 10 < price_for_contract <= 30:
        price_for_mobile_network = 4.35
    elif price_for_contract > 30:
        price_for_mobile_network = 3.85

money_for_contract = (price_for_contract + price_for_mobile_network) * number_of_months_to_pay
if time_for_contract == 'two':
    price = money_for_contract - (money_for_contract * 3.75) / 100
else:
    price = money_for_contract
print(f'{price:.2f} lv.')
