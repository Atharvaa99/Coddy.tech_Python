text = input()
count = 0
for char in text:
    if "p" in char or "P" in char:
        count += 1
print(count)  