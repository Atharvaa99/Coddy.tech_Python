def prod(lst):
    result = 1
    for i in range(len(lst)):
        result *= lst[i]
    return result