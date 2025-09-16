def check_inventory(inventory,item):
    if item in inventory:
        print(f"{item} is in stock. Quantity: {inventory[item]}")
    else:
        print(f"{item} is not in stock.")
