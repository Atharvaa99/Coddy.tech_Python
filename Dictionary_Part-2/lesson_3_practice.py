def print_product_details(product_data):
    if not product_data:
        print("No product information available")
    for key,value in product_data.items():
        print(f"{key.capitalize()}: {value}")