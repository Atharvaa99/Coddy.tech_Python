def sum_nested(nested_list):
    sum_list = 0
    for element in nested_list:
        if isinstance(element,list):
            sum_list += sum_nested(element)
        else:
            sum_list += element
    return sum_list