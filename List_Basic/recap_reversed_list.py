def reverse(lst):
    n = len(lst)
    for i in range(n // 2):
        temp = lst[i]
        lst[i] = lst[n-i-1]
        lst[n-i-1] = temp
    return lst