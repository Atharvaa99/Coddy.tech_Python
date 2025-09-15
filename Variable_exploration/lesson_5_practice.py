def calculate_discount(price,discount_percentage):
    discount_amount = (price * discount_percentage)/100
    new_price = price - discount_amount
    return round(new_price,2)

result = calculate_discount(75.5,10)
print(result)