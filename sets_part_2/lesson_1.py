def set_operations(set1,set2):
    union_result = set1 | set2
    intersection_result = set1 & set2
    difference_result = set1 - set2
    symmetric_difference = set1 ^ set2

    return {
            "union": union_result,
            "intersection": intersection_result,
            "difference": difference_result,
            "symmetric_difference": symmetric_difference
    }