def find_occurrences(text,pattern):
    count = 0
    occurred = False
    lst = []
    pattern_length = int(len(pattern))
    for i in range(0,len(text) - pattern_length + 1): 
      if pattern == text[i:i + pattern_length]:
            count += 1
            occurred = True
            lst.append(i)
    tup = (occurred,count,lst)
    return tup

text = input()
pattern = input()
result = find_occurrences(text,pattern)
print(result)
