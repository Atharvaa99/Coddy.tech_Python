try:
    ip = int(input())
    print(f"You entered: {ip}")
except ValueError:
    print("Invalid input! Please enter a valid number.")