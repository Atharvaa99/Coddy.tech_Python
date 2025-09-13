print("Welcome to the Daily Expense Tracker!\n")
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
lst = []
while True:
    choice = int(input())
    if choice == 1:
        expense = float(input())
        lst.append(expense)
        print("Expense added successfully!")
    elif choice == 2:
        continue
    elif choice == 3:
        continue
    elif choice == 4:
        continue
    elif choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break