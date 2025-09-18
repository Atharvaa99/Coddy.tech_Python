def compare_strings(str1, str2):

    is_substring = str1 in str2
    starts_with = str2.startswith(str1)
    ends_with = str2.endswith(str1)
    equals = str1.lower() == str2.lower()
    
    dict_str = {"is_substring": is_substring,
                "starts_with": starts_with,
                "ends_with": ends_with,
                "is_equal": equals}
    return dict_str