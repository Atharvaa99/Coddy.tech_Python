numbers = input().split(',')
result = 0
for num in numbers:
    if int(num) % 2 == 0:
       result += int(num)
print(result) 