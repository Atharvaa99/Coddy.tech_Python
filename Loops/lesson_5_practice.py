# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
for i in range(30,81):
    if i % 4 == 0:
        print(i, end=", ")

print()  # new line
# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
for i in range(15,30,2):
    print(i, end=", ")

print()  # new line
# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
for i in range(50,9,-5):
    print(i, end=", ")

print()  # new line
# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
product = 1
for i in range(1,31):
    if i % 3 == 0:
        product *= i

print(product)
