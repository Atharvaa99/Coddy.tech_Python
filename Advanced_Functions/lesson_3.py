number = int(input())
categorize_number = lambda num: "Positive" if num > 0 else "Zero" if num == 0 else "Negative"
print(categorize_number(number))