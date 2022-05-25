name_of_the_flightcompany = input()
number_of_adult_tickets = int(input())
number_of_kids_tickets = int(input())
net_price_for_ticket_for_adult = float(input())
price_for_service = float(input())
profit_for_agency = 0

net_price_for_kid_ticket = (70 * net_price_for_ticket_for_adult) / 100
net_price_for_ticket_for_kid = net_price_for_ticket_for_adult - net_price_for_kid_ticket
full_price_for_ticket_for_kid = net_price_for_ticket_for_kid + price_for_service
net_price_for_ticket_for_adult = net_price_for_ticket_for_adult + price_for_service
profit_for_agency = (full_price_for_ticket_for_kid * number_of_kids_tickets) + \
                    (net_price_for_ticket_for_adult * number_of_adult_tickets)
full_profit_for_agency = (profit_for_agency * 20) / 100

print(f'The profit of your agency from {name_of_the_flightcompany} tickets is {full_profit_for_agency:.2f} lv.')