def helper_function(num):
    if num <=0:
        return False
    return True

def process_numbers(numbers):
    filtered_nums = filter(helper_function,numbers)
    triple_double_nums = map(lambda x: x*2 if x % 2 == 0 else x*3,filtered_nums)
    return list(triple_double_nums)