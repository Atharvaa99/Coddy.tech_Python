names = ["Alice", "Bob", "Charlie"]
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

alice = "Alice is in the list." if "Alice" in names else "Alice is not in the list."
david = "David is in the list." if "David" in names else "David is not in the list."
bob = "Bob is in the dictionary." if "Bob" in grades else "Bob is not in the dictionary."
eve = "Eve is in the dictionary." if "Eve" in grades else "Eve is not in the dictionary."

print(alice)
print(david)
print(bob)
print(eve)