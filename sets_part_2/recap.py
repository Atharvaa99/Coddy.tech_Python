match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

all_matches = match1 & match2 & match3
match_1_only = match1 - match2 - match3

unique_set = (match1 | match2) | match3
unique_num = len(unique_set)

one_match_set1 = match1 - match2 - match3
one_match_set2 = match2 - match1 - match3
one_match_set3 = match3 - match2 - match1
only_one_match = one_match_set1 | one_match_set2 | one_match_set3

two_match_set1 = match1 & match2
two_match_set2 = match2 & match3
two_match_set3 = match1 & match3
temp = two_match_set1 | two_match_set2 | two_match_set3
two_match = temp - all_matches

print(f"Players in all matches: {sorted(list(all_matches))}")
print(f"Players in exactly two matches: {sorted(list(two_match))}")
print(f"Players in only one match: {sorted(list(only_one_match))}")
print(f"Total unique players: {unique_num}")
print(f"Players in Match 1 only: {sorted(list(match_1_only))}")