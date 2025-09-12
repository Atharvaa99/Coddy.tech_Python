numbers = input().split()
lst = numbers + numbers[::-1]
lst1 = []
lst1.append(numbers[0])
lst2 = lst1 + lst
lst2.append(numbers[len(numbers)-1])
lst = lst2 * 2
print(lst)