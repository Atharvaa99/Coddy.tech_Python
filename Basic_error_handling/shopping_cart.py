def handle_shopping_cart(orders):
    order_dict = {}
    for order in orders:
        try:
            if ":" in order:
                order_split = order.split(':')
                if int(order_split[1]) >= 0:
                    if order_split[0] not in order_dict:
                        order_dict[order_split[0]] = int(order_split[1])
                    else:
                         order_dict[order_split[0]] += int(order_split[1])
                else:
                    print(f"Negative quantity not allowed: {order}")
            else:
                print(f"Invalid format: {order}")
        except ValueError:
                print(f"Invalid quantity: {order}")            
        

    return order_dict 