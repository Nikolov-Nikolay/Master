stage_from_tournament = input()
kind_of_ticket = input()
number_of_tickets = int(input())
photo_with_trophy = input()
price_for_ticket = 0
final_price_for_all_tickets = 0

if stage_from_tournament == 'Quarter final':
    if kind_of_ticket == 'Standard':
        price_for_ticket = 55.50
    elif kind_of_ticket == 'Premium':
        price_for_ticket = 105.20
    elif kind_of_ticket == 'VIP':
        price_for_ticket = 118.90
elif stage_from_tournament == 'Semi final':
    if kind_of_ticket == 'Standard':
        price_for_ticket = 75.88
    elif kind_of_ticket == 'Premium':
        price_for_ticket = 125.22
    elif kind_of_ticket == 'VIP':
        price_for_ticket = 300.40
elif stage_from_tournament == 'Final':
    if kind_of_ticket == 'Standard':
        price_for_ticket = 110.10
    elif kind_of_ticket == 'Premium':
        price_for_ticket = 160.66
    elif kind_of_ticket == 'VIP':
        price_for_ticket = 400

price_for_all_tickets = price_for_ticket * number_of_tickets
if price_for_all_tickets > 4000:
    price_for_all_tickets = price_for_all_tickets - ((price_for_all_tickets * 25) / 100)
elif 4000 > price_for_all_tickets > 2500:
    price_for_all_tickets = price_for_all_tickets - (price_for_all_tickets * 10) / 100
if photo_with_trophy == 'Y':
    price_for_all_tickets += (number_of_tickets * 40)
    if price_for_all_tickets > 4000:
        price_for_all_tickets -= (number_of_tickets * 40)
elif photo_with_trophy == 'N':
    pass

print(f'{price_for_all_tickets:.2f}')
