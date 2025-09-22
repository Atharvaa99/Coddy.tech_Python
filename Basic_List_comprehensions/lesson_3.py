def filter_and_square(numbers):
    positive_num_square = [ num ** 2 for num in numbers if num > 0]
    return positive_num_square