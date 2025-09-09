lst = list(map(int, input().split(",")))
# Write your code below
indices = []
for index, item in enumerate(lst):
    if int(item) < 50 or int(item) % 5 == 0:
        indices.append(index)
print(indices)