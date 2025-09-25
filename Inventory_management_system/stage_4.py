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

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"
    
