def elements_of_freedom(string_list):
    filter_list = [strings.upper() for strings in string_list if len(strings)>=5 ]
    removing_duplicate = []
    for string in filter_list:
        if string in removing_duplicate:
            continue
        else:
            removing_duplicate.append(string)
    return removing_duplicate