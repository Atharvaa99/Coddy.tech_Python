lst = input().split(",")
newlst = []
for item in lst:
    if len(item) > 5:
       newlst.append(item)
print(newlst)