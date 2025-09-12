lst1 = input().split(',')
lst2 = input().split(',')
lst3 = []
for i in range(len(lst1)):
    if lst1[i] in lst2:
        continue
    else:
        lst3.append(lst1[i])
print(lst3)