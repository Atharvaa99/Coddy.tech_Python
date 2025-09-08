def combine_and_filter(lst, threshold):
    lst1 = []
    for i in range(len(lst)):
        if lst[i] > threshold:
            lst1.append(lst[i])
    lst1.sort()
    return lst1