lst = input().split(",")
lst1 = lst[1::3]
print(lst1)
lst2temp = lst[:6]
lst2 = lst2temp[-6:]
print(lst2[::-1])
middle = len(lst)//2
lst3 = lst[middle::2]
print(lst3)