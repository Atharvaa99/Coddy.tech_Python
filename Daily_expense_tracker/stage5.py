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
        if len(lst) > 0:
            print("Your expenses:")
            for index,expense in enumerate(lst):
                print(f"{index+1}. {expense}")
        else:
            print("No expenses recorded yet.")
    elif choice == 3:
        if len(lst) > 0:
            total_expense = sum(lst)
            average_expense = total_expense / len(lst)
            print(f"Total expense: {total_expense}")
            print(f"Average expense: {average_expense}")
        else:
            print("No expenses recorded yet.")
    elif choice == 4:
        continue
    elif choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
