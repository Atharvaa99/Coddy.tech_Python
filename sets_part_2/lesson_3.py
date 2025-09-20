region1 = eval(input())
region2 = eval(input())
region3 = eval(input())

all_treasures = region1 | region2 | region3
unique_treasures_region1 = region1 - region2 - region3
shared_treasures = region1 & region2 & region3
set1 = region1 - region2 - region3
set2 = region2 - region1 - region3
set3 = region3 - region2 - region1
exclusive_treasures = set1 | set2 | set3

print("Shared treasures:", sorted(list(shared_treasures)))
print("Unique treasures in region1:", sorted(list(unique_treasures_region1)))
print("All treasures:", sorted(list(all_treasures)))
print("Exclusive treasures:", sorted(list(exclusive_treasures)))