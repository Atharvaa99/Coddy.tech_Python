def iterate_and_filter_set(input_set):
    output_set = set()
    for num in input_set:
        if num <= 10:
            output_set.add(num)

    return output_set