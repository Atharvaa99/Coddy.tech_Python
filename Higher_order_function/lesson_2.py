def get_long_strings(strings):
    filtered_strings = filter(lambda x: len(x) > 5,strings)
    return list(filtered_strings)