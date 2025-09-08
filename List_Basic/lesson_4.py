def merge(lst1, lst2):
    for i in range(len(lst2)):
        lst1.append(lst2[i])
        lst1.sort()
    print(lst1)