input_list = input().split(', ')
if len(input_list) >= 5:
    res = input_list[:2] + input_list[-2:]
else:
    res = [input_list[0], input_list[-1]]
print(res)