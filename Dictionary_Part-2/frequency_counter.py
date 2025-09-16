def frequency_counter(data_list):
    counter = {}
    for items in data_list:
        if items not in counter:
            counter[items] = 1
        else:
            counter[items] += 1
    return counter