def order_func(order_dict, command):
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product in order_dict:
        order_dict[product] = [price, (quantity + order_dict[product][1])]
    else:
        order_dict[product] = [price, quantity]

    return order_dict


def orders():

    order_dict = {}

    while True:
        command = input()

        if command == 'buy':
            break

        command = command.split(' ')
        order_dict = order_func(order_dict, command)

    for k in order_dict:
        total_sum = order_dict[k][0] * order_dict[k][1]
        print(f'{k} -> {total_sum:.2f}')


orders()
