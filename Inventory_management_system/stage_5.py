inventory = {}

def add_item(item:str,price:float,stock:int):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {'price': price, 'stock':stock}
        print(f"Item '{item}' added successfully.")

def update_stock(item:str,quantity:int):   
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        new_stock = quantity + inventory[item]['stock']
        if new_stock< 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]['stock'] = new_stock
            print(f"Stock for '{item}' updated successfully.")

def check_availability(item:str):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]['stock']

def sales_report(sales):
    total_revenue = 0
    for item in sales:
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
        else:
            if inventory[item]['stock'] >= sales[item]:
                inventory[item]['stock'] -= sales[item]
                total_revenue += sales[item] * inventory[item]['price']
            else:
                 print(f"Error: Insufficient stock for '{item}'")              
    print(f"Total revenue: ${total_revenue:.2f}")

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
sales_report(sales)  # Should output: 19.0
print(inventory)
