def dictionary_sorter(data_dict):
    new_dict = {}
    value_list = []
    for key in data_dict:
        value_list.append(data_dict[key])
    sorted_value = sorted(value_list)
    for i in range(0,len(sorted_value)):
        for key in data_dict:
            if data_dict[key] == sorted_value[i]:
                new_dict[key] = sorted_value[i]
    return new_dict