def not_mutual_friends(lst1,lst2):
    lst3 = []
    for friend in lst1:
        if friend not in lst2:
            lst3.append(friend)
        else:
            continue
    for friend in lst2:
        if friend not in lst1:
            lst3.append(friend)
        else:
            continue
    return lst3