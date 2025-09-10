lst = input().split()
indices = []
for index, word in enumerate(lst):
    if len(word) > 3 or word.startswith("a"):
        indices.append(index) 
print(indices)