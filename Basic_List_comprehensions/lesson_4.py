def sum_positive_evens(numbers):
    sum_even = sum([n for n in numbers if (n>0 and (n%2 == 0))])
    return sum_even