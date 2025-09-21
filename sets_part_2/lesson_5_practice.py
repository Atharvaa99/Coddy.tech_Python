def filter_and_square_set(input_set):
    square_odd_set = set()
    for num in input_set:
        if (num & 1) == 0 :
            continue
        else:
            square_odd_set.add(num ** 2)

    return square_odd_set