numbers = input()
prefix = input()
# Write your code below
lst = numbers.split()
for i in range(len(lst)):
    lst[i] = prefix + lst[i]
string = ' '.join(lst)
print(string)