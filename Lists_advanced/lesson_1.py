lst = input().split(",")
if len(lst) % 2 == 0:
    start = len(lst)//2 -1
    end = start + 2
    print(lst[start:end])
else:
    start = len(lst)//2 - 1
    end = start + 3
    print(lst[start:end])