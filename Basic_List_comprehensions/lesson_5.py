def house_of_lists(list_of_lists):
    filter_lists = [lists for lists in list_of_lists if sum(lists) < 50]
    nums = [n for nums in filter_lists for n in nums if n < 5]
    return nums