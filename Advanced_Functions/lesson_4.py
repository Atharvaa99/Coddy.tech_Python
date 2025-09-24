def sort_tuples(data):
    sorted_tuple = sorted(data, key = lambda x: (x[1],x[0]))
    return sorted_tuple