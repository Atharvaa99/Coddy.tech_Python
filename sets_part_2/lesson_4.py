def check_sets(set1,set2):
    is_subset = set1 <= set2
    is_superset = set2 >= set1
    is_proper_superset = set2 > set1
    is_proper_subset = set1 < set2
    
    return{
            "is_subset": is_subset,
            "is_superset": is_superset,
            "is_proper_subset":is_proper_subset,
            "is_proper_superset": is_proper_superset
    }