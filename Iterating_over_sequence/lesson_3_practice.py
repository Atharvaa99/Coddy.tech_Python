text = input()
count = 0
for char in text:
    if "s" in char or "S" in char:
        count += 1
print(count)