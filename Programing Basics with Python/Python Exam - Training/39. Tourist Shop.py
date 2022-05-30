budget = float(input())
price = 0
number_of_products = 0
discount = 0

while True:
    name_of_the_product = input()
    if name_of_the_product == 'Stop':
        print(f'You bought {number_of_products} products for {price:.2f} leva.')
        break

    product_price = float(input())
    number_of_products = number_of_products + 1
    if number_of_products % 3 == 0:
        price = price + product_price / 2
    else:
        price += product_price
    if price > budget:
        print(f"You don't have enough money!You need {price - budget:.2f} leva!")
        break




