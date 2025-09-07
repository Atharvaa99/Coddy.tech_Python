def calculation():
    res = 0
    for i in range(10001):
        res += i
    print(res)

num = int(input())
for i in range(num):
    calculation()
